from django.db import models

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'book' 
