from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .models import User
from .models import Useradmin
from .forms import CareerApplicationForm
from .models import Career
from .models import Employee
from .models import Payroll
from .models import Attendance
from .models import Leave
from .models import Asset
from .models import DocumentUpload
from .models import Resign
from .forms import DocumentUploadForm
from .forms import ResignationForm 
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.utils.timezone import now
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import os

def home(request):
    return render(request,"navbar.html")

#employee personal 
def employeepersonal(request):
    employeename = request.session.get('employeename')  # Get employee name from session

    if not employeename:
        return redirect('login')  # Redirect to login if session is not set

    try:
        user = Employee.objects.get(employeename=employeename)  # Fetch only the logged-in employee's data
        return render(request, 'emppersonal.html', {'user': user})

    except Employee.DoesNotExist:
        return HttpResponse("Employee details not found", status=404)

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password != cpassword:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        user = User.objects.create_user(username=name, email=email, password=password)
        messages.success(request, "Your account has been registered successfully. Please log in.")
        return redirect('login')

    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)  # Get user by email
            authenticated_user = authenticate(request, username=user.username, password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)
                request.session['name'] = user.username  # Store username in session
                return redirect('employee')  # Redirect to Employee Dashboard
            else:
                messages.error(request, "Invalid email or password. Please try again.")
                return redirect('login')

        except User.DoesNotExist:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('login')

    return render(request, 'base.html') 

# password reset and confirm 

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_sent.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

@login_required
def dashboard(request):
        user=User.objects.all()
        admin_email = "hragrace22@gmail.com"
        user_email = request.user.email
        # Pass a flag to the template to allow/disallow editing
        return render(request, "dashboard-base.html", {"is_admin": user_email == admin_email})

#employee crud
def employee(request):
    return render(request,"employee.html")

def create2(request):
    if request.user.is_authenticated:  # Ensure user is logged in
        try:
            # Check if employee already exists using email
            employee = Employee.objects.get(gmail=request.user.email)
            request.session['employeename'] = employee.employeename  # Store in session
            return redirect('read2')  # Redirect to `read2` if data exists
        except Employee.DoesNotExist:
            pass  # Allow form submission if user doesn't exist

    if request.method == 'POST':
        employeename = request.POST.get('employeename')  # Get employee name

        user = Employee(
            employeename=employeename,
            lastname=request.POST.get('lastname'),
            employeeid=request.POST.get('employeeid'),
            gmail=request.POST.get('gmail'),
            age=request.POST.get('age'),
            date=request.POST.get('date'),
            gender=request.POST.get('gender'),
            mobile=request.POST.get('mobile'),
            department=request.POST.get('department'),
            qualification=request.POST.get('qualification'),
            fathername=request.POST.get('fathername'),
            mothername=request.POST.get('mothername'),
            fathercontact=request.POST.get('fathercontact'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            country=request.POST.get('country'),
            status=request.POST.get('status'),
            workdepartment=request.POST.get('workdepartment'),
            experience=request.POST.get('experience'),
            worklocation=request.POST.get('worklocation'),
            salary=request.POST.get('salary'),
            joindate=request.POST.get('joindate'),
            shifttime=request.POST.get('shifttime'),
            employeetype=request.POST.get('employeetype'),
        )

        if 'picture' in request.FILES:
            user.picture = request.FILES['picture']

        user.save()

        # Store employeename in session for use in all pages
        request.session['employeename'] = employeename

        return redirect('read2')

    return render(request, "employee.html")

def read2(request):
    employeename = request.session.get('employeename')  # Retrieve session data

    if not employeename:
        return redirect('login')  # Redirect to login if session is empty

    try:
        user = Employee.objects.get(employeename=employeename)  # Fetch a single employee object
        context = {'user': user}  # Pass as an object, not a list
        return render(request, "empdashboard.html", context)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found", status=404)

##update the employee code

def update_employee(request, user_id):
    if request.method == "POST":
        # Ensure employee exists
        user = get_object_or_404(Employee, id=user_id)

        # Update employee fields
        user.employeename = request.POST.get("employeename", user.employeename)
        user.lastname = request.POST.get("lastname", user.lastname)
        user.employeeid = request.POST.get("employeeid", user.employeeid)
        user.gmail = request.POST.get("gmail", user.gmail)
        user.age = request.POST.get("age", user.age)
        user.date = request.POST.get("date", user.date)
        user.gender = request.POST.get("gender", user.gender)
        user.mobile = request.POST.get("mobile", user.mobile)
        user.department = request.POST.get("department", user.department)
        user.qualification = request.POST.get("qualification", user.qualification)
        user.fathername = request.POST.get("fathername", user.fathername)
        user.mothername = request.POST.get("mothername", user.mothername)
        user.fathercontact = request.POST.get("fathercontact", user.fathercontact)
        user.address = request.POST.get("address", user.address)
        user.city = request.POST.get("city", user.city)
        user.state = request.POST.get("state", user.state)
        user.country = request.POST.get("country", user.country)
        user.status = request.POST.get("status", user.status)
        user.workdepartment = request.POST.get("workdepartment", user.workdepartment)
        user.experience = request.POST.get("experience", user.experience)
        user.worklocation = request.POST.get("worklocation", user.worklocation)
        user.salary = request.POST.get("salary", user.salary)
        user.joindate = request.POST.get("joindate", user.joindate)
        user.shifttime = request.POST.get("shifttime", user.shifttime)
        user.employeetype = request.POST.get("employeetype", user.employeetype)

        # Save updates
        user.save()

        return redirect('read2')  # Make sure 'emppersonal' is a valid URL name

    return redirect('read2') 
# attendance crud page

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        attend = Attendance(
            employeename = request.POST.get('employeename'),
            employeeid = request.POST.get('employeeid'),
            department = request.POST.get('department'),
            mobile= request.POST.get('mobile'),
            indate= request.POST.get('indate'),
            intime= request.POST.get('intime'),
            outtime= request.POST.get('outtime'),
        )
        attend.save()
        return redirect('read')
        context={'attend': attend}
    return render(request,"index.html",context)


def read(request):
    employeename = request.session.get('employeename')
    if not employeename:
        return redirect('login')  # Redirect if user is not logged in

    employee = get_object_or_404(Employee, employeename=employeename)
    today = now().date()

    # Check if an attendance record already exists for today
    attend = Attendance.objects.filter(employeename=employee, indate=today).first()

    # If no record exists, create a new one
    if not attend:
        attend = Attendance.objects.create(
            employeename=employee, 
            indate=today, 
            status='Not Informed'
        )

    if request.method == "POST":
        attend.status = "Pending"
        attend.intime = request.POST.get('intime')
        attend.outtime = request.POST.get('outtime')
        attend.save()
        return redirect('read')

    # Fetch all attendance records of the user
    attend = Attendance.objects.filter(employeename=employee).order_by('-indate')

    return render(request, 'index.html', {'attend': attend})

#payroll crud

def emppayroll(request):
    return render(request,'emppayroll.html')

def create3(request):
    if request.method == 'POST':
        pay = Payroll(
            employeename = request.POST.get('employeename'),
            employeeid = request.POST.get('employeeid'),
            department = request.POST.get('department'),
            bankname= request.POST.get('bankname'),
            bankbranch= request.POST.get('bankbranch'),
            accountnumber= request.POST.get('accountnumber'),
            code= request.POST.get('code'),
            bankcode= request.POST.get('bankcode'),
            branchaddress=request.POST.get('branchaddress')
        )
        pay.save()
        return redirect('read3')
        context={'pay': pay}
    return render(request,"emppayroll.html",context)

def read3(request):
    employeename = request.session.get('employeename')  # Get employee name from session

    if not employeename:
        return redirect('login')  # Redirect to login if no session is found

    try:
        pay = Payroll.objects.filter(employeename=employeename)  # Filter payroll for this user
        return render(request, "emppayroll.html", {'pay': pay})

    except Payroll.DoesNotExist:
        return HttpResponse("Payroll records not found", status=404)

# leave request crud
def empleave(request):
    return render(request,'empleave.html')

def create4(request):
    if request.method == 'POST':
        leave = Leave(
            employeename = request.POST.get('employeename'),
            employeeid = request.POST.get('employeeid'),
            department = request.POST.get('department'),
            startdate= request.POST.get('startdate'),
            enddate= request.POST.get('enddate'),
            requestday= request.POST.get('requestday'),
        )
        leave.save()
        return redirect('read4')
        context={'leave': leave}
    return render(request,"empleave.html",context)

def read4(request):
    employeename = request.session.get('employeename')  # Get employee name from session

    if not employeename:
        return redirect('login')  # Redirect to login if no session is found

    try:
        leave = Leave.objects.filter(employeename=employeename)  # Filter leave records for this user
        return render(request, "empleave.html", {'leave': leave})

    except Leave.DoesNotExist:
        return HttpResponse("Leave records not found", status=404)
    
# Career page

def empcareer(request):
      return render(request,'empcareer.html')   

def apply_job(request):
    if request.method == "POST":
        form = CareerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.status = "Pending"
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('empcareer')  # Or wherever you want to go
        else:
            messages.error(request, "Error submitting application. Check the form.")
            print("❌ Form errors:", form.errors)

    form = CareerApplicationForm()
    return render(request, 'empcareer.html', {'form': form}) 

#Employee Asset
def empasset(request):
    return render(request,'empassets.html')

def create5(request):
    if request.method == 'POST':
        asset = Asset(
            employeename = request.POST.get('employeename'),
            assets= request.POST.get('assets'),
            assetname = request.POST.get('assetname'),
            assigndate= request.POST.get('assigndate'),
            batchno= request.POST.get('batchno'),
            assignby= request.POST.get('assignby'),
        )
        asset.save()
        return redirect('read5')
        context={'asset': asset}
    return render(request,"empassets.html",context)

def read5(request):
    employeename = request.session.get('employeename')  # Get employee name from session

    if not employeename:
        return redirect('login')  # Redirect to login if no session found

    asset = Asset.objects.filter(employeename=employeename)  # Fetch all assets for this user

    return render(request, "empassets.html", {'asset': asset})

#File Uploads
def upload_documents(request):
    if request.method == 'POST':
        print("Received POST request 🚀")
        print("CSRF Token:", request.POST.get('csrfmiddlewaretoken'))  # Print CSRF token
        print("Name:", request.POST.get('employeename'))  # Print user-entered name
        print("FILES:", request.FILES)  # Print all uploaded files (binary format)

        # Debug: Print individual file data
        for key, file in request.FILES.items():
            print(f"{key}: ({file.content_type}) - {file.size} bytes")  # Show file type & size

        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("✅ Form is valid. Saving files...")
            form.save()
            messages.success(request, 'Your file has been uploaded successfully!')
            return redirect('document_list')
        else:
            print("❌ Form errors:", form.errors)
            messages.error(request, 'There was an error in your form. Please check your inputs.')

    else:
        form = DocumentUploadForm()

    documents = DocumentUpload.objects.all()
    return render(request, 'empdoc.html', {'form': form, 'documents': documents})

def document_list(request):
    employeename = request.session.get('employeename')  # Get employee name from session

    if not employeename:
        return redirect('login')  # Redirect to login if session is not set

    # Fetch only the logged-in employee's documents
    documents = DocumentUpload.objects.filter(employeename=employeename)

    return render(request, 'empdoc.html', {'documents': documents})

## emp resign 

def empresign(request):
    employeename = request.session.get('employeename')  # Get employee name from session
    if not employeename:
        return redirect('login')  # Redirect to login if session is not set

    resign = Resign.objects.filter(employeename=employeename)  # Fetch only the logged-in employee's resignations
    return render(request, 'empresign.html', {'resign': resign})


def resignation_submit(request):
    if request.method == "POST":
        form = ResignationForm(request.POST, request.FILES)
        if form.is_valid():
            resign = form.save(commit=False)  
            resign.status = "Pending"  # Set default status
            resign.save()  
            messages.success(request, "Your resignation has been submitted.")
            return redirect('empresign')
        else:
            messages.error(request, "Error submitting resignation. Please check the form.")
            print("❌ Form errors:", form.errors)  # Debugging
    
    form = ResignationForm()
    resign = Resign.objects.all()
    return render(request, 'empresign.html', {'form': form, 'resign': resign})
    
#user side mail send
@csrf_exempt
def contact_form_submit(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        contact_no = data.get("contact_no")
        description = data.get("description")

        subject = "New Contact Form Submission"
        message = f"""
        Name: {name}
        Email: {email}
        Contact No: {contact_no}
        Description: {description}
        """
        admin_email = "n2sagracetech@gmail.com"  #  admin email
        send_mail(subject, message, email, [admin_email])

        return JsonResponse({"message": "Email sent successfully!"}, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)

#user side excel export
def export_data_attend(request):

    data = Attendance.objects.all().values()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="attendance.xlsx"'
    df.to_excel(response, index=False, engine="openpyxl")

    return response

#////////////////////admin side user ///////////////

def ensure_admin():
    email = "agracea22@gmail.com"
    user, created = User.objects.get_or_create(email=email, defaults={"username": "admin"})
    
    if created or not user.is_superuser:
        user.is_staff = True
        user.is_superuser = True
        user.set_password("agrace@2002")  # Change this to a secure password
        user.save()
        print("Admin user ensured:", email)

ensure_admin()  # Call this function at the start

def adminsignup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword', '')  # Default to empty string if missing

        if password != cpassword:
            messages.error(request, "Passwords do not match!")
            return redirect('adminsignup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('adminsignup')

        user = User.objects.create_user(username=name, email=email, password=password)
        messages.success(request, "Your account has been registered successfully. Please log in.")
        return redirect('adminlogin')

    return render(request, 'custom/adminlogin.html')

def adminlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)  # Get user by email
            authenticated_user = authenticate(request, username=user.username, password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('admin_dashboard')  # Redirect to Employee Dashboard
            else:
                messages.error(request, "Invalid email or password. Please try again.")
                return redirect('adminlogin')

        except User.DoesNotExist:
            messages.error(request, "Invalid email or password. Please try again.")
            return redirect('adminlogin')

    return render(request, 'custom/adminlogin.html')
 
# ✅ Admin Dashboard
@login_required
def admin_dashboard(request):
    employeename = Employee.objects.count()
    male_count = Employee.objects.filter(gender="Male").count()
    female_count = Employee.objects.filter(gender="Female").count()
    context = {
        "employeename": employeename,
        "male_count" : male_count,
        "female_count" :female_count,
    }

    return render(request, "custom/admindashboard.html",context)

# ✅ Admin Logout
@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def adminemployee(request):
    user=Employee.objects.all()
    context={'user':user}
    return render(request,'custom/adminemployee.html',context)

def adminemppersonal(request, id):
    user = get_object_or_404(Employee, id=id)  # Get employee by ID
    return render(request, 'custom/adminemppersonal.html', {'user': user})

def admincareer(request):
    applications = Career.objects.all().order_by('-id')  # Latest first
    return render(request, 'custom/admincareer.html', {'applications': applications})


def update_status(request, app_id):
    if request.method == "POST":
        data = json.loads(request.body)
        new_status = data.get('status')
        try:
            app = Career.objects.get(id=app_id)
            app.status = new_status
            app.save()
            return JsonResponse({'success': True})
        except Career.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

def send_career_email(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        gmail = request.POST.get('gmail')
        jobrole = request.POST.get('jobrole')
        status = request.POST.get('status')

        subject = f"Application Update - {jobrole}"
        message = f"Hello {fullname},\n\nYour application for the role of {jobrole} has been updated to: {status}.\n\nBest regards,\nHR Team"
        # Update the following with your actual sender email.
        sender_email = 'hr@example.com'
        try:
            send_mail(subject, message, sender_email, [gmail])
            messages.success(request, "Mail sent successfully.")
        except Exception as e:
            messages.error(request, f"Error sending email: {e}")
        return redirect('admincareer')

def adminattendance(request):
    selected_date = request.GET.get('date', now().date())  # Filter by date
    attend = Attendance.objects.filter(indate=selected_date)

    return render(request, 'custom/adminattend.html', {'attend': attend, 'selected_date': selected_date})

# Function to update status (Present/Absent)
def updateattendance(request, id, status):
    try:
        attend = Attendance.objects.get(id=id)
        attend.status = status
        attend.save()
        return JsonResponse({'success': True, 'status': status})
    except Attendance.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Attendance record not found'})

def adminleave(request):
    leave=Leave.objects.all()
    context={'leave':leave}
    return render(request,'custom/adminleave.html',context)

def updateleave(request, id, status):
    try:
        leave = Leave.objects.get(id=id)
        leave.status = status
        leave.save()
        print(f"Updated Leave ID {id} to {status}")  # Debugging print
        return JsonResponse({'success': True, 'status': leave.status})
    except Leave.DoesNotExist:
        print("Leave record not found")  # Debugging print
        return JsonResponse({'success': False, 'error': 'Leave record not found'}, status=404)

def admindocument(request):
    documents=DocumentUpload.objects.all()
    context={'documents':documents}
    return render(request,'custom/admindocument.html',context)

def adminassets(request):
    asset=Asset.objects.all()
    context={'asset':asset}
    return render(request,'custom/adminasset.html',context)

def update_asset_status(request, id, status):
    """Update asset status (Active, Inactive, Returned)"""
    try:
        asset = get_object_or_404(Asset, id=id)
        asset.status = status
        asset.save()

        return JsonResponse({'success': True, 'status': asset.status})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

def return_asset(request, id):
    """Mark asset as returned and update message field"""
    try:
        asset = get_object_or_404(Asset, id=id)
        asset.status = "Returned"
        asset.message = f"Your asset '{asset.assetname}' has been returned."
        asset.save()

        return JsonResponse({'success': True, 'status': "Returned", 'message': asset.message})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


def adminpayroll(request):
    pay=Payroll.objects.all()
    context={'pay':pay}
    return render(request,'custom/adminpayroll.html',context)

@csrf_exempt 
def updatepayment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  
            print("Received Data:", data)  

            pay_id = data.get("id")  
            status = data.get("status")

            if not pay_id or not status:
                return JsonResponse({'success': False, 'error': 'Missing parameters'}, status=400)

            pay = Payroll.objects.get(id=pay_id)
            pay.status = status
            pay.save()

            return JsonResponse({'success': True, 'status': pay.status})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Payroll.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Payment record not found'}, status=404)
    
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

def adminresign(request):
    resign = Resign.objects.all()  
    return render(request, 'custom/adminresign.html', {'resign': resign})


def update_resign_status(request, resign_id, status):
    resign = get_object_or_404(Resign, id=resign_id)
    resign.status = status  # Update to Approved/Rejected
    resign.save()
    
    messages.success(request, f"Resignation {status}.")
    return redirect('adminresign')  # Redirect to the admin page

#excel data export
def export_data(request):

    data = Employee.objects.all().values()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="employees.xlsx"'
    df.to_excel(response, index=False, engine="openpyxl")

    return response

#Admin side mail send
@csrf_exempt
def send_employee_mail(request):
    if request.method == "POST":
        employee_name = request.POST.get("employee_name")
        employee_email = request.POST.get("employee_email")
        message = request.POST.get("message")

        if not employee_email or not message:
            return JsonResponse({"status": "error", "message": "Email and Message are required!"})

        # Email subject & content
        subject = f"Message from Admin - {employee_name}"
        email_body = f"Dear {employee_name},\n\n{message}\n\nBest Regards,\nYour Admin"

        try:
            send_mail(subject, email_body, "n2sagracetech@gmail.com", [employee_email])
            return JsonResponse({"status": "success", "message": "Email sent successfully!"})
        except Exception as e:
            logger.error(f"Error sending email: {str(e)}")  # Log the error for better debugging
            return JsonResponse({"status": "error", "message": f"Error: {str(e)}"})

    return JsonResponse({"status": "error", "message": "Invalid request method."})