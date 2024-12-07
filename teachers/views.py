from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


def home(request):
    return render(request, 'index.html')


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})


def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        if (first_name and last_name
                and subject):
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject,

            )
            return redirect('teachers:teacher_list')
    return render(request, 'teachers/add_teacher.html')


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:teacher_list')
