from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    button1 = models.CharField(max_length=50)
    button2 = models.CharField(max_length=50)
    url1 = models.CharField(max_length=50)
    url2 = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class GeneralSettings(models.Model):
    logo = models.ImageField(upload_to='images')
    email1 = models.CharField(max_length=100)
    email2 = models.CharField(max_length=100)
    tel1 = models.CharField(max_length=100)
    tel2 = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.email1

class Program(models.Model):
    program_name = models.CharField(max_length=200)

    def __str__(self):
        return self.program_name

class Update(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    free = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', null=True)
    date = models.CharField(max_length=50)

    def __str__(self):
        return self.title