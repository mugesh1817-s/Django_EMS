def admin_status(request):
    admin_email = "hragrace22@gmail.com"
    return {"is_admin": request.user.email == admin_email if request.user.is_authenticated else False}
