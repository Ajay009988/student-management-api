from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

@login_required
def dashboard(request):
    if request.user.is_superuser:
        students = Student.objects.all().order_by('-id')
    else:
        students = Student.objects.filter(owner=request.user).order_by('-id')
    
    q = request.GET.get('q')
    if q:
        students = students.filter(name__icontains=q)
    return render(request, 'dashboard.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            s = form.save(commit=False)
            s.owner = request.user
            s.save()
            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required
def delete_student(request, id):
    s = Student.objects.get(id=id)
    if request.user.is_superuser or s.owner == request.user:
        s.delete()
    return redirect('dashboard')