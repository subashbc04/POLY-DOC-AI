from django.db import models

class analyse(models.Model):
    document=models.FileField(upload_to='doc/')
    queries=models.TextField(max_length=800)

