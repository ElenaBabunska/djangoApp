from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FlowerCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    height = models.CharField(max_length=50, null=True, blank=True)
    grow_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(FlowerCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="covers")

    def __str__(self):
        return self.name


class Reminder(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Garden(models.Model):
    name = models.CharField(max_length=50)
    flower = models.ManyToManyField(Flower)
    private = models.BooleanField()
    reminder = models.ForeignKey(Reminder, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Answer(models.Model):
    content = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Question(models.Model):
    content = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content
