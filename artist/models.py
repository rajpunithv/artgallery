from django.db import models


# Create your models here.
class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'login_table'

    def __str__(self):
        return self.username


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    artistid = models.BigIntegerField(blank=False, unique=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))  # tuple
    gender = models.CharField(max_length=10, blank=False, choices=gender_choices)
    password = models.CharField(max_length=100, blank=False, default="klu123")
    email = models.CharField(max_length=100, blank=False, unique=True)
    contact = models.CharField(max_length=100, blank=False, unique=True)

    class Meta:
        db_table = "artist_table"

    def __str__(self):
        return self.username


from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
