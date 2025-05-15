"""
URL configuration for myprojectattend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('custom-admin/', include('myapp.urls')), 
    path('', views.home, name="home"),
    path('index/', views.index, name='index'),
    path('empcareer/',views.empcareer,name='empcareer'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_view,name="login"),
    path('employee/',views.create2,name="employee"),
    path('emppersonal/',views.employeepersonal,name='employeepersonal'),
    path('empleave/',views.empleave,name='empleave'),
    path('emppayroll/',views.emppayroll,name='emppayroll'),
    path('empasset/',views.empasset,name='empasset'),
    path('create/',views.create,name='create'),
    path('read/',views.read,name='read'),
    # path('dashboard/', views.dashboard, name="dashboard"),
    # CRUD URLs
    # path('update_employee/<int:id>/', views.update_employee, name='update_employee'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    path('create2/',views.create2,name='create2'),
    path('read2/',views.read2,name='read2'),
    path('update_employee/<int:user_id>/',views.update_employee, name='update_employee'),
    # path("export/", views.export_data, name="export_data"),
    path('create3/',views.create3,name='create3'),
    path('read3/',views.read3,name='read3'),
    # path('adminpayroll',views.adminpayroll,name="adminpayroll"),
    path('create4/',views.create4,name='create4'),
    path('read4/',views.read4,name='read4'),

    path('create5/',views.create5,name='create5'),
    path('read5/',views.read5,name='read5'),

    path('upload_documents/',views.upload_documents, name='upload_documents'),
    path('document-list/',views.document_list, name='document_list'),
    path('empresign/', views.empresign, name='empresign'),
    path('apply/', views.apply_job, name='apply_job'),
    path('resignation/submit/', views.resignation_submit, name='resignation_submit'),
     path("submit-contact-form/",views.contact_form_submit, name="submit_contact_form"),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # admin site urls
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    

