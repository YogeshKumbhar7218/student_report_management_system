from dataclasses import field, fields
from django import forms
from .models import Teacher_stack_student_activities

class Activities(forms.ModelForm):

    class Meta:
        model = Teacher_stack_student_activities
        fields = ('img','desc','stud_id')
