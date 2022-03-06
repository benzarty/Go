from django.views.generic import ListView,CreateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project, Student
from .forms import StudentForm, StudentModelForm

# Create your views here.
def homePage(request):
    return HttpResponse('<h1>hahahaha</h1>')

def list_Student(request):
    list = Student.objects.all() #recuper tout les etudiant
    context = {
        'list_students':list,
    }
    return render(request, 'hub/list.html',{'list_students':list,})


def detail_student(request,id):
    student = Student.objects.get(id=id)  #get_object_or_404(Student,pk=id)
    return render(request, 'hub/details.html',{'student':student,})


def listprojet(request):
    list = Project.objects.all() #recuper tout les etudiant

    return render(request, 'hub/listprojet.html',{'object_list':list})

class ProjectLissstView(ListView):
    model=Project
    template_name='hub/listprojet.html'
    # geenret une vue basé sur modele 






def addStudent(request):
    # print(request.POST) 
    if request.method == "POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")


        Student.objects.create(
             firstname=firstname,
             lastname=lastname,
             email=email

        )
        return redirect('student_displayyyyyyyyy')


    return render(request,'hub/addstudent.html')


def addstudentform(request):
    form=StudentForm()

    if request.method == "POST":
      form=StudentForm(request.POST)
      if form.is_valid():

        Student.objects.create(

             firstname=form.cleaned_data.get('firstname'),

             lastname=form.cleaned_data['lastname'],

             email=form.cleaned_data['email']

        )
      return redirect('student_displayyyyyyyyy')


    return render(request,'hub/addFormsss.html',{'form' : form})      
   


def addstudentmodelformm(request):
      form=StudentModelForm()

      if request.method == "POST":
       form=StudentModelForm(request.POST)
       if form.is_valid():

        student=form.save()
        return redirect('student_displayyyyyyyyy')


      return render(request,'hub/addFormsss.html',{'form' : form})  


class StudentCreateView(CreateView):
    model = Student
    form_class=StudentModelForm
    template_name='hub/addFormsss.html' 