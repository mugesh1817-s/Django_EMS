from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Employee
from .models import Payroll
from .models import Attendance
from .models import Leave
from .models import Asset
from .models import DocumentUpload
from .models import Resign
from .models import Career
from .models import BiometricAttendance
from .models import BiometricEmployee

# Unregister the default User model first
admin.site.unregister(User)

admin.site.register(Employee)

admin.site.register(Payroll)

admin.site.register(Attendance)

admin.site.register(Leave)

admin.site.register(Asset)

admin.site.register(DocumentUpload)

admin.site.register(Resign)

admin.site.register(Career)

admin.site.register(BiometricAttendance)

admin.site.register(BiometricEmployee)


# Register it again with custom settings
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass  # You can add custom admin settings here

