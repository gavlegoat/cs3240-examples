from django.db import models

class UploadFile(models.Model):
    file_field = models.FileField(upload_to="documents")
