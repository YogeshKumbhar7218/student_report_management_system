from django.contrib import admin

from catalog.models import Authenticate, Student, Department, Year, Semester, Subjects, Term1, Term2, Final,Teacher_stack_student_activities

# Register your models here.
@admin.register(Authenticate)
class AuthenticateAdmin(admin.ModelAdmin):
    list_display = ("en_roll_no","user_name","passwd","email","parent_user_name","parent_passwd")



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("stud_id","name","dept_id","roll_no","current_year")

admin.site.register(Department)
admin.site.register(Year)
admin.site.register(Semester)


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ("sub_name","sub_id","dept_id","sem_no") 


@admin.register(Term1)
class Term1Admin(admin.ModelAdmin):
    list_display = ("stud_id","marks","out_of","sub_id","sem_no")


@admin.register(Term2)
class Term2Admin(admin.ModelAdmin):
    list_display = ("stud_id","marks","out_of","sub_id","sem_no")


@admin.register(Final)
class FinalAdmin(admin.ModelAdmin):
    list_display = ("stud_id","marks","out_of","sub_id","sem_no")


@admin.register(Teacher_stack_student_activities)
class Teacher_stack_student_activitiesAdmin(admin.ModelAdmin):
    list_display = ("stud_id","approved","points","points","desc","img")

