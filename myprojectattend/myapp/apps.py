from django.apps import AppConfig
import sys
import logging

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        # Prevent running during commands that initialize the DB or system
        if any(cmd in sys.argv for cmd in ['makemigrations', 'migrate', 'collectstatic', 'shell']):
            return

        try:
            from django.contrib.auth.models import User
            from django.db.utils import OperationalError

            email = "agracea22@gmail.com"
            user, created = User.objects.get_or_create(email=email, defaults={"username": "admin"})

            if created or not user.is_superuser:
                user.is_staff = True
                user.is_superuser = True
                user.set_password("agrace@2002")
                user.save()
                print("✅ Admin user ensured:", email)

        except OperationalError:
            logging.warning("Skipping ensure_admin due to DB not being ready")
        except Exception as e:
            logging.error(f"Unexpected error in ensure_admin: {e}")
