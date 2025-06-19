from django.db import models
from django.contrib.auth.models import User

class QuestionPaper(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)  # link to uploader account
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=50)
    year = models.IntegerField()
    slot = models.CharField(max_length=10)
    faculty = models.CharField(max_length=100)
    file = models.FileField(upload_to='question_papers/')
    is_approved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_code} - {self.course_name} ({self.year})"
