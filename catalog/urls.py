from urllib import request
from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('sign_up/',views.sign_up, name ='sign_up'),
    
    path('sign_up/student_sign_up/',views.student_sign_up, name ='student_sign_up'),
    path('sign_up/student_sign_up/student_sign_up',views.student_sign_up, name ='student_sign_up2'),
    path('sign_up/parent_sign_up/',views.parent_sign_up, name ='parent_sign_up'),
    path('sign_up/parent_sign_up/parent_sign_up',views.parent_sign_up, name ='student_sign_up2'),

    path('login/',views.login, name ='login'),
    path('login/student_login/',views.student_login, name ='student_login'),
    path('login/student_login/student_login',views.student_login, name ='student_login2'),
    path('login/parent_login/',views.parent_login, name ='parent_login'),
    path('login/parent_login/parent_login',views.parent_login, name ='parent_login2'),
    path('login/teacher_login/',views.teacher_login, name ='teacher_login'),
    
    
    # path('login/student_login/logout',views.logout, name ='logout'),
    path('login/student_login/logout',views.logout, name ='logout'),
    path('login/parent_login/logout',views.logout, name ='logout2'),


    path('login/parent_login/result',views.result, name ='result'),
    path('login/student_login/result',views.result, name ='result'),


    path('login/parent_login/sem1',views.sem1, name ='sem1'),
    path('login/parent_login/sem2',views.sem2, name ='sem2'),
    path('login/parent_login/sem3',views.sem3, name ='sem3'),
    path('login/parent_login/sem4',views.sem4, name ='sem4'),
    path('login/parent_login/sem5',views.sem5, name ='sem5'),
    path('login/parent_login/sem6',views.sem6, name ='sem6'),
    path('login/parent_login/sem7',views.sem7, name ='sem7'),
    path('login/parent_login/sem8',views.sem8, name ='sem8'),
  
    path('login/student_login/sem1',views.sem1, name ='sem1'),
    path('login/student_login/sem2',views.sem2, name ='sem2'),
    path('login/student_login/sem3',views.sem3, name ='sem3'),
    path('login/student_login/sem4',views.sem4, name ='sem4'),
    path('login/student_login/sem5',views.sem5, name ='sem5'),
    path('login/student_login/sem6',views.sem6, name ='sem6'),
    path('login/student_login/sem7',views.sem7, name ='sem7'),
    path('login/student_login/sem8',views.sem8, name ='sem8'),
    path('login/student_login/sem',views.sem, name ='sem'),

  
    path('login/student_login/extra_activities',views.extra_activities, name ='extra_activities'),
    path('login/student_login/add_activity',views.add_activity, name ='add_activity'),

    path('login/parent_login/extra_activities',views.extra_activities, name ='extra_activities'),
    path('login/parent_login/add_activity',views.add_activity, name ='add_activity'),


]