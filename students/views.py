from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student


@login_required
def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        {"students": students}
    )


@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Student added successfully!")

            return redirect("student_list")

    else:

        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {"form": form}
    )