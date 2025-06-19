from django import forms
from .models import QuestionPaper

class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['course_name', 'course_code', 'year', 'slot', 'faculty', 'file']
