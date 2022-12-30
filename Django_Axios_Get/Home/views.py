from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from Home.models import Student,Course,Subject

def home(request):
    h_temp = loader.get_template('home.html')
    return HttpResponse(h_temp.render())

def show(request):

    

    # for student in students:
    #     print(student.name)
    #     print(student.dob)
    #     print(student.course_enrolled.course_name)
    #     print(student.subject_chosen.subject_name)
    #     print("\n")

    
    st_temp = loader.get_template('students.html')

    return HttpResponse(st_temp.render())


def display(request):

    students = Student.objects.all()

    context = {
        "students":students

    }

    get_temp = loader.get_template('get_details.html')
    return HttpResponse(get_temp.render(context,request))


@csrf_exempt
def add(request):

    if request.method  == 'GET':
        a_temp = loader.get_template('add.html')

        return HttpResponse(a_temp.render())

    if request.method == 'POST':
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        subject = request.POST.get('subject')
        dob = request.POST.get('dob')
        print(name,degree,subject,dob)
        status = {
            "status":'Server Side is Okay'
        }

        return JsonResponse(status)

def get_degrees(request):
    
    degrees = Course.objects.all()
    
    d_temp = loader.get_template('degrees.html')
    context = {
        "degrees":degrees,
        
    }

    return HttpResponse(d_temp.render(context,request))



def get_subjects(request,id):
    if request.method=='GET':
        # id = request.GET.get('degree')
        s_temp = loader.get_template('subjects.html')

        subjects = Subject.objects.filter(course_name__id = id)
        context = {
            "subjects":subjects,
        }
        return HttpResponse(s_temp.render(context,request))


            
