
from django.db import models

class Resume(models.Model):
    pdf = models.FileField(upload_to='resumes/')