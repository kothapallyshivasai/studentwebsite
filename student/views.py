from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

def home_page(request):
    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.is_authenticated:
            return redirect("/student/student_home")
 
    except Exception as e:
        return render(request, "index.html", {})
 
    else:
        return render(request, "index.html", {})
    
@login_required
@never_cache
def student_home_page(request):
    return render(request, "student_home.html", {"object": Student.objects.get(pk = request.user.username)})

@login_required
@never_cache
def student_attendance(request):
    student = Student.objects.get(pk = request.user.username)
    attendance = Attendance.objects.filter(student_roll_number = student.student_roll_number).first()
    return render(request, "student_attendance_graph.html", {"object": student, "attendance": attendance})

@login_required
@never_cache
def contact_us(request):
    success = request.GET.get("success")
    return render(request, "student_contact_us.html", {"success":success, "object": Student.objects.get(pk = request.user.username)})

@login_required
@never_cache
def display_marks(request, year):
    student = Student.objects.get(pk=request.user.username)
    marks = StudentMarks.objects.filter(roll_number=student.student_roll_number, year=year).first()
    subjects = BranchSubjects.objects.filter(branch=student.student_branch, year=year).first()
    try:
        grade1 = return_grade(marks.subject_1)
        grade2 = return_grade(marks.subject_2)
        grade3 = return_grade(marks.subject_3)
        grade4 = return_grade(marks.subject_4)
    except Exception as e:
        return render(request, "display_marks.html", {"condition": True})

    return render(request, "display_marks.html", {"object": Student.objects.get(pk = request.user.username), 'marks': marks, 'subjects': subjects, 'grade1': grade1, 'grade2': grade2,
                                                     'grade3': grade3, 'grade4': grade4,})

@login_required
@never_cache
def submit_contact_us(request):
    if request.method == "POST":
        contact_us = ContactUs()
        contact_us.student_roll_number = request.POST.get("roll_number")
        contact_us.subject = request.POST.get("subject")
        contact_us.message = request.POST.get("message")
        try:
            contact_us.save()
            return redirect("/student/contact_us?success=OK")
        except Exception as e:
            return redirect("/student/contact_us?success=NO")
    else:
        return redirect("/student/contact_us")
    
@login_required
@never_cache
def course(request):
    student = Student.objects.get(pk=request.user.username) 
    branch_details = BranchDetails.objects.get(branch = student.student_branch)
    return render(request, "course.html", {"student": student, "branch": branch_details})

@login_required
@never_cache
def personal_information(request):
    student = Student.objects.get(pk=request.user.username)
    return render(request, "personal_information.html", {'student': student})


@login_required
@never_cache
def academic_information(request):
    return redirect("/student/home")



def test(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect("/student/home")
    else:
        form = UserCreationForm()
        
    return render(request, "test.html", {'form': form})

def return_grade(marks):
    
    if marks == 100:
        return "O"
    
    elif marks >= 90:
        return "A+"
    
    elif marks >= 80:
        return "A"
    
    elif marks >= 70:
        return "B+"
    
    elif marks >= 60:
        return "B"
    
    elif marks >= 50:
        return "C+"
    
    elif marks >= 35:
        return "C"
    
    else:
        return "F"

def custom_404_view(request, exception):
    del exception
    return render(request, '404.html', {}, status=404)