from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50,default=False)
    email = models.EmailField(max_length=50,db_index=False)  # Reduce max_length
    password = models.CharField(max_length=128)  # Increase for hashed passwords
    conformpassword=models.CharField(max_length=50,default=False)

class Useradmin(models.Model):
    name = models.CharField(max_length=50,default=False)
    email = models.EmailField(max_length=50,db_index=False)  # Reduce max_length
    password = models.CharField(max_length=128)  # Increase for hashed passwords
    conformpassword=models.CharField(max_length=50,default=False)

class Employee(models.Model):
    employeename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, null=True)
    employeeid = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=15, null=True)
    date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    fathername=models.CharField(max_length=30,default=False,null=True)
    mothername=models.CharField(max_length=30,default=False,null=True)
    fathercontact=models.CharField(max_length=30,default=False,null=True)
    address=models.CharField(max_length=50,default=False,null=True)
    city=models.CharField(max_length=35,default=False,null=True)
    state=models.CharField(max_length=30,default=False,null=True)
    country=models.CharField(max_length=30,default=False,null=True)
    status=models.CharField(max_length=20,default=False,null=True)
    workdepartment=models.CharField(max_length=30,default=False,null=True)
    experience = models.CharField(max_length=20,null=True)
    worklocation=models.CharField(max_length=30,default=False,null=True)
    salary = models.CharField(max_length=10, null=True)
    joindate = models.DateField(null=True, blank=True)
    shifttime=models.CharField(max_length=30,default=False,null=True)
    employeetype=models.CharField(max_length=30,default=False,null=True)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)

    def __str__(self):
        return self.employeename

class Payroll(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]
    employeename = models.CharField(max_length=100)
    employeeid = models.CharField(max_length=50)
    department = models.CharField(max_length=100, null=True)
    bankname=models.CharField(max_length=30,default=False,null=True)
    bankbranch=models.CharField(max_length=40,default=False,null=True)
    accountnumber=models.CharField(max_length=12,default=False,null=True)
    code=models.CharField(max_length=12,default=False,null=True)
    bankcode=models.CharField(max_length=20,default=False,null=True)
    branchaddress=models.CharField(max_length=50,default=False,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') 

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Not Informed', 'Not Informed'),
    ]
    employeename = models.CharField(max_length=100)
    employeeid = models.CharField(max_length=50)
    department = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=15, null=True)
    indate=models.DateField(auto_now=True)
    intime=models.TimeField(default="09:00:00",null=True)
    outtime=models.TimeField(default="17:00:00",null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Informed')
    
class Leave(models.Model):
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    employeename = models.CharField(max_length=100)
    employeeid = models.CharField(max_length=50)
    department = models.CharField(max_length=100, null=True)
    startdate=models.DateField(auto_now=True)
    enddate=models.DateField(auto_now=True)
    requestday=models.CharField(max_length=20,default=False,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  

class Asset(models.Model):
    employeename = models.CharField(max_length=100)
    assets=models.CharField(max_length=30)
    assetname=models.CharField(max_length=30)
    assigndate=models.DateField(auto_now=True)
    batchno=models.CharField(max_length=30)
    assignby=models.CharField(max_length=30)
    status = models.CharField(max_length=20, default="Active")
    message = models.CharField(max_length=100, blank=True, null=True)

class DocumentUpload(models.Model):
    employeename = models.CharField(max_length=255)  # User name
    tenth_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    twelth_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    graduate_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    professional_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    aadhar_card = models.FileField(upload_to='documents/', blank=True, null=True)
    pan_card = models.FileField(upload_to='documents/', blank=True, null=True)
    passport = models.FileField(upload_to='documents/', blank=True, null=True)
    driving_license = models.FileField(upload_to='documents/', blank=True, null=True)
    medical_certificate = models.FileField(upload_to='documents/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Resign(models.Model):
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    employeename = models.CharField(max_length=255)
    employeeid=models.CharField(max_length=30)
    department=models.CharField(max_length=100,null=True,blank=True)
    gmail=models.CharField(max_length=40,null=True)
    mobile=models.CharField(max_length=20)
    resignationletter = models.FileField(upload_to='letters/', blank=True, null=True)
    leavedate=models.DateField(auto_now=True)
    reason=models.CharField(max_length=50)
    status = models.CharField(max_length=20, default="Pending", blank=True, null=True) 

class Career(models.Model):
    STATUS_CHOICES = [
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    fullname = models.CharField(max_length=255)
    gmail = models.EmailField(max_length=255)
    jobrole = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="Pending", blank=True, null=True) 



class BiometricEmployee(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BiometricAttendance(models.Model):
    employee = models.ForeignKey(BiometricEmployee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=10, default='IN')

    def __str__(self):
        return f"{self.employee.name} - {self.timestamp}"
