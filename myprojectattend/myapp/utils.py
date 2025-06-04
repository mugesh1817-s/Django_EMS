from zk import ZK
from django.utils import timezone
from datetime import date
import datetime
from myapp.models import BiometricAttendance, BiometricEmployee, Leave

def sync_attendance():
    zk = ZK('192.168.1.201', port=4370, timeout=5)

    try:
        conn = zk.connect()
        conn.disable_device()
        attendance_records = conn.get_attendance()
        count = 0
        today = timezone.localdate()

        # ✅ Skip if today is Sunday
        if today.weekday() == 6:  # 0 = Monday, ..., 6 = Sunday
            print("✅ Sunday: No attendance or leave recorded.")
            return 0

        present_ids = set()

        for record in attendance_records:
            employee, _ = BiometricEmployee.objects.get_or_create(
                user_id=record.user_id,
                defaults={'name': f"User {record.user_id}"}
            )

            timestamp = timezone.make_aware(record.timestamp)
            if timestamp.date() == today:
                present_ids.add(employee.id)

            obj, created = BiometricAttendance.objects.get_or_create(
                employee=employee,
                timestamp=timestamp,
                defaults={'status': 'IN'}
            )

            if created:
                count += 1

        # ✅ Mark leave for absentees (except on Sundays)
        all_employees = BiometricEmployee.objects.all()
        for emp in all_employees:
            if emp.id not in present_ids:
                if not Leave.objects.filter(employeeid=emp.user_id, startdate=today).exists():
                    Leave.objects.create(
                        employeename=emp.name,
                        employeeid=emp.user_id,
                        department=getattr(emp, 'department', 'Unknown'),
                        startdate=today,
                        enddate=today,
                        requestday="1"
                    )

        conn.enable_device()
        conn.disconnect()
        return count

    except Exception as e:
        print(f"❌ Sync error: {e}")
        return 0
