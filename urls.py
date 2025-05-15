from django.urls import path
from myapp import views

urlpatterns = [
    path('adminsignup/', views.adminsignup, name="adminsignup"),  
    path('adminlogin/', views.adminlogin, name="adminlogin"),  
    path('dashboard/', views.admin_dashboard, name="admin_dashboard"),  
    path('logout/', views.admin_logout, name="admin_logout"),
    path('admincareer/', views.admincareer, name='admincareer'),
    path('adminemployee/',views.adminemployee,name="adminemployee"),
    path('adminemppersonal/<int:id>/',views.adminemppersonal, name='adminemppersonal'),
    path('adminattendance/',views.adminattendance,name="adminattendance"),
    path('updateattendance/<int:id>/<str:status>/',views.updateattendance, name='updateattendance'),
    path('adminleave/',views.adminleave,name="adminleave"),
    path('updateleave/<int:id>/<str:status>/', views.updateleave, name='updateleave'),
    path('admindocument/',views.admindocument,name="admindocument"),
    path('adminassets/',views.adminassets,name="adminassets"),
    path('update_asset_status/<int:id>/<str:status>/',views.update_asset_status, name='update_asset_status'),
    path('return_asset/<int:id>/',views.return_asset, name='return_asset'),
    path('adminpayroll/',views.adminpayroll,name="adminpayroll"),
    path("updatepayment/",views.updatepayment, name="updatepayment"),
    path('adminresign/',views.adminresign, name='adminresign'),
    path('update_resign_status/<int:resign_id>/<str:status>/',views.update_resign_status, name='update_resign_status'),
    path("export_attend/", views.export_data, name="export_data"),
    path("export/", views.export_data_attend, name="export_data_attend"),
    path("send-mail/",views.send_employee_mail, name="send_employee_mail"),
    path('update-status/<int:app_id>/',views.update_status, name='update_status'),
    path('send-career-email/',views.send_career_email, name='send_career_email'),
    
]