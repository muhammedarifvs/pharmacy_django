from django.urls import path
from . import views

urlpatterns=[
    path("",views.homepage,name='homepage'),
    path("about",views.aboutus,name='aboutus'),
    path("registration",views.signup,name='signup'),
    path("login",views.loginpage,name='loginpage'),
    path("contact",views.contactpage,name='contactpage'),
    path('doctor',views.doctorspage,name='doctorspage'),
    path('departments',views.departmentpage,name='departmentpage'),
    path('medicines<int:depadmin_id>',views.medicinepage,name='medicinepage'),
    path('formpage',views.adddep,name='adddep'),
    path('update<int:depadmin_id>',views.updatedep,name='updatedep'),
    path('delete<int:depadmin_id>',views.deletedep,name='deletedep')

]