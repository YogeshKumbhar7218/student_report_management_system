from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import EmailField

# Create your models here.

class Authenticate(models.Model):
    en_roll_no = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
    email = EmailField()
    parent_user_name= models.CharField(max_length=20,null=True)
    parent_passwd = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.en_roll_no}, {self.user_name}, {self.passwd}, {self.email}, {self.parent_user_name}, {self.parent_passwd}"


class Student(models.Model):
    name = models.CharField(max_length=50)
    stud_id = models.IntegerField(primary_key=True)
    roll_no = models.IntegerField()
    current_year = models.ForeignKey("Year",on_delete=models.CASCADE)
    dept_id = models.ForeignKey("Department",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stud_id}, {self.roll_no}, {self.name}, {self.dept_id}, {self.current_year}"


class Department(models.Model):
    name = models.CharField(max_length=50)
    dept_id = models.IntegerField(primary_key=True)

class Year(models.Model):
    year_no = models.IntegerField(primary_key=True)

class Semester(models.Model):
    sem_no = models.IntegerField(primary_key=True)

class Subjects(models.Model):
    sub_name = models.CharField(max_length=50)
    sub_id = models.IntegerField(primary_key=True)
    dept_id = models.ForeignKey("Department",on_delete=models.CASCADE)
    year_no = models.ForeignKey("Year",on_delete=models.CASCADE)
    sem_no = models.ForeignKey("Semester",on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.sub_name}, {self.sub_id}, {self.dept_id}, {self.sem_no}"


class Term1(models.Model):
    stud_id =models.ForeignKey("Student",on_delete=models.CASCADE)
    marks = models.IntegerField()
    out_of = models.IntegerField()
    sub_id = models.ForeignKey("Subjects",on_delete=models.CASCADE)
    sem_no =models.ForeignKey("Semester",on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.stud_id}, {self.marks}, {self.out_of}, {self.sub_id}, {self.sem_no}"

class Term2(models.Model):
    stud_id =models.ForeignKey("Student",on_delete=models.CASCADE)
    marks = models.IntegerField()
    out_of = models.IntegerField()
    sub_id = models.ForeignKey("Subjects",on_delete=models.CASCADE)
    sem_no =models.ForeignKey("Semester",on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.stud_id}, {self.marks}, {self.out_of}, {self.sub_id}, {self.sem_no}"

class Final(models.Model):
    stud_id =models.ForeignKey("Student",on_delete=models.CASCADE)
    marks = models.IntegerField()
    out_of = models.IntegerField()
    sub_id = models.ForeignKey("Subjects",on_delete=models.CASCADE)
    sem_no =models.ForeignKey("Semester",on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.stud_id}, {self.marks}, {self.out_of}, {self.sub_id}, {self.sem_no}"


class Teacher_stack_student_activities(models.Model):

    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    # stud_id =models.ForeignKey("Student",on_delete=models.CASCADE)
    stud_id = models.IntegerField()
    approved = models.CharField(max_length=5, null=True)
    points = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.stud_id}, {self.approved}, {self.points}, {self.desc}, {self.img}"
   
class Activity:
    img : str
    desc : str
    # stud_id =models.ForeignKey("Student",on_delete=models.CASCADE)
    stud_id :int
    approved : str
    points : int


