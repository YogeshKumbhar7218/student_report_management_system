from pickletools import int4
import re
from unicodedata import name
from unittest import result
from wsgiref.util import request_uri
from django import forms
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Activity, Authenticate, Student, Semester, Subjects,Term1,Term2,Final,Teacher_stack_student_activities
from django.db import connection
from .forms import Activities
# Create your views here.

def index(request):
    return render(request,'index.html')

def sign_up(request):
    return render(request,'signUp.html')

def student_sign_up(request):
    if request.method=='GET':
        return render(request,'studentSignUp.html')
    elif request.method=='POST':
        user_name = request.POST['uname']
        passwd = request.POST['passwd']
        en_roll_no = int(request.POST['student_enroll_no'])
        email = request.POST['email']
        
        #if allready not exitst do register
        #if exist then do redirect
        if not Authenticate.objects.filter(en_roll_no=en_roll_no).exists() and not Authenticate.objects.filter(user_name=user_name).exists():
            user = Authenticate()
            user.en_roll_no=en_roll_no
            user.user_name=user_name
            user.passwd=passwd
            user.email=email
            user.save()
            return HttpResponse('SignUp Successfull!')
        else : 
            return HttpResponse('User Already Exists! ')
            

        # check the account already exists or not
        # if account exist then return error 
        # if account does'nt exist do register
        

def parent_sign_up(request):
    # return render(request,'parentSignUp.html')
    if request.method=='GET':
        return render(request,'parentSignUp.html')
    elif request.method=='POST':
        user_name = request.POST['uname']
        passwd = request.POST['passwd']
        en_roll_no = int(request.POST['student_enroll_no'])
        # email = request.POST['email']
        
        #if allready not exitst do register
        #if exist then do redirect
        if not Authenticate.objects.filter(en_roll_no=en_roll_no).exists():
            return HttpResponse("Your child not registerd yet!")
        elif Authenticate.objects.filter(parent_user_name=user_name).exists(): 
            return HttpResponse("User already exists!")
        else:
            Authenticate.objects.filter(en_roll_no=en_roll_no).update(parent_user_name=user_name,parent_passwd=passwd)
            return HttpResponse("SignUp Successful!")

        


def login(request):
    return render(request,'login.html')

def student_login(request):
    if request.method=='GET':
        return render(request,'student_login.html')
    elif request.method=='POST':
        user_name = request.POST['uname']
        passwd = request.POST['passwd']
        if Authenticate.objects.filter(user_name=user_name).exists():
            user = Authenticate.objects.get(user_name=user_name)
            if user.passwd==passwd :
                request.session['login_status'] = 'in'
                request.session['en_roll_no'] = user.en_roll_no
                return render(request,'user.html')
            else :
                return HttpResponse("Wrong Id or Password")

        else:
            return HttpResponse("This account doesnt exist")
            
            
        

def parent_login(request):
    if request.method=='GET':
        return render(request,'parent_login.html')
    elif request.method=='POST':
        user_name = request.POST['uname']
        passwd = request.POST['passwd']
        if Authenticate.objects.filter(parent_user_name=user_name).exists():
            user = Authenticate.objects.get(parent_user_name=user_name)
            if user.parent_passwd==passwd :
                request.session['login_status'] = 'in'
                request.session['en_roll_no'] = user.en_roll_no
                return render(request,'user.html')
            else :
                return HttpResponse("Wrong Id or Password")
        else:
            return HttpResponse("This account doesnt exist")
def teacher_login(request):
   return redirect('/admin')

def logout(request):
    request.session['login_status'] = 'out'
    del request.session['en_roll_no'] 
    return redirect('/')


def result(request):
    return render(request,'sem_menu.html')


def sem1(request):
    request.session['sem'] = '1'
    return redirect(sem)

    

def sem2(request):
    request.session['sem'] = '2'
    return redirect(sem)

def sem3(request):
    request.session['sem'] = '3'
    return redirect(sem)

def sem4(request):
    request.session['sem'] = '4'
    return redirect(sem)

def sem5(request):
    request.session['sem'] = '5'
    return redirect(sem)

def sem6(request):
    request.session['sem'] = '6'
    return redirect(sem)


def sem7(request):
    request.session['sem'] = '7'
    return redirect(sem)

def sem8(request):
    request.session['sem'] = '8'
    return redirect(sem)

def sem(request):
    print(request.session['sem'])
    sem = request.session['sem']
    print(sem)

    #1. obtain marks for term 1 
    cursor = connection.cursor()
    cursor.execute('SELECT sub_name, marks, out_of FROM catalog_term1,catalog_subjects WHERE catalog_term1.sub_id_id=catalog_subjects.sub_id AND catalog_subjects.sem_no_id='+sem+' AND catalog_term1.stud_id_id='+str(request.session['en_roll_no'])+';')
    term1 = cursor.fetchall()
    # print(term1)

    cursor.execute('SELECT sub_name, marks, out_of FROM catalog_term2,catalog_subjects WHERE catalog_term2.sub_id_id=catalog_subjects.sub_id AND catalog_subjects.sem_no_id='+sem+' AND catalog_term2.stud_id_id='+str(request.session['en_roll_no'])+';')
    term2 = cursor.fetchall()
    # print(term2)

    cursor.execute('SELECT sub_name, marks, out_of FROM catalog_final,catalog_subjects WHERE catalog_final.sub_id_id=catalog_subjects.sub_id AND catalog_subjects.sem_no_id='+sem+' AND catalog_final.stud_id_id='+str(request.session['en_roll_no'])+';')
    final = cursor.fetchall()
    # print(final)
    

    size = len(term1)
    data = {'subjects':['Subject Name','Marks Obtained','Total Marks']} 
    for i in range(size):
        sub_name = 'subjectt1'+str(i+1)
        data.update({sub_name:[term1[i][0],term1[i][1],term1[i][2]]})

    #1. obtain marks for term 2 
        #cal percentage
    size = len(term2)
    for i in range(size):
        sub_name = 'subjectt2'+str(i+1)
        data.update({sub_name:[term2[i][0],term2[i][1],term2[i][2]]})

    #1. obtain marks for final 
        #percnetage

    size = len(final)
    for i in range(size):
        sub_name = 'subjectfinal'+str(i+1)
        data.update({sub_name:[final[i][0],final[i][1],final[i][2]]})
    return render(request,"sem1.html",data)



def extra_activities(request):
    if request.method=='GET':
        acts = Teacher_stack_student_activities.objects.all().filter(stud_id=int(request.session['en_roll_no'])) and Teacher_stack_student_activities.objects.all().filter(approved='yes')    
        return render(request, 'extra_activities.html', {'acts': acts,'media_url':settings.MEDIA_URL})



def add_activity(request):
    if request.method=='GET':
        form = Activities()
        return render(request, 'add_activity.html', {'form': form})        
    elif request.method=='POST':
        form = Activities(request.POST, request.FILES)
        if form.is_valid():

            print( type(form.cleaned_data['stud_id']))

            if form.cleaned_data['stud_id'] == int(request.session['en_roll_no']):
                form.save()
            else :
                return render(request,'error.html')
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'add_activity.html', {'form': form, 'img_obj': img_obj})