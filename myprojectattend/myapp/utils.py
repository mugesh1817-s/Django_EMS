from zk import ZK
from django.utils import timezone
from myapp.models import BiometricAttendance, BiometricEmployee  # Replace with your actual app

def sync_attendance():
    zk = ZK('192.168.1.201', port=4370, timeout=5)

    try:
        conn = zk.connect()
        conn.disable_device()
        attendance_records = conn.get_attendance()
        count = 0

        for record in attendance_records:
            employee, _ = BiometricEmployee.objects.get_or_create(
                user_id=record.user_id,
                defaults={'name': f"User {record.user_id}"}
            )

            obj, created = BiometricAttendance.objects.get_or_create(
                employee=employee,
                timestamp=timezone.make_aware(record.timestamp),
                defaults={'status': 'IN'}
            )

            if created:
                count += 1

        conn.enable_device()
        conn.disconnect()
        return count

    except Exception as e:
        print(f"Sync error: {e}")
        return 0
