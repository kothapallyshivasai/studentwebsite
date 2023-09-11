from django.urls import path
from .views import test, home_page, student_home_page, student_attendance, contact_us, submit_contact_us, display_marks, course, personal_information, academic_information
from django.contrib.auth import views
from django.views.decorators.cache import never_cache

urlpatterns = [
    path("home/", home_page, name="home"),
    path('login/', views.LoginView.as_view(template_name=""'student_login.html'), name="login"),
    path('student_home/', student_home_page, name="student_home"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('attendance/', student_attendance, name="attendance"),
    path('change_password/', never_cache(views.PasswordChangeView.as_view(template_name="student_change_password.html")), name="change_password"),
    path('password_change_done/', never_cache(views.PasswordChangeDoneView.as_view(template_name='student_password_change_done.html')), name='password_change_done'),
    path('contact_us/', contact_us, name="contact_us"),
    path('display_marks/<str:year>', display_marks, name="display_marks"),
    path('submit_contact_us/', submit_contact_us, name='submit_contact_us'),
    path('personal_information/', personal_information, name='personal_information'),
    path('course/', course, name='course'),
    path('academic_information/', academic_information, name='academic_information'),
    path('test/', test)
] 