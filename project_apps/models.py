from django.db import models
# Create your models here.


class Users(models.Model):
    userName = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    phoneNum = models.CharField(max_length=15, default=0)
    email = models.CharField(max_length=50)
    group = models.CharField(max_length=25)


class Courses(models.Model):
    courseName = models.CharField(max_length=100)
    courseNum = models.CharField(max_length=4, default=0000)
    courseTime = models.TimeField()
    courseDay = models.CharField(max_length=15, default=None)
    instructorFirstName = models.CharField(max_length=50)
    instructorLastName = models.CharField(max_length=50)
    taFirstName = models.CharField(max_length=50)
    taLastName = models.CharField(max_length=50)


class Labs(models.Model):
    courseNum = models.CharField(max_length=100)
    labNum = models.IntegerField()
    labTime = models.CharField(max_length=50)
    taFirstName = models.CharField(max_length=50)
    taLastName = models.CharField(max_length=50)


class CourseAssign(models.Model):
    courseName = models.CharField(max_length=100)
    assignmentNum = models.IntegerField()
    assignment = models.CharField(max_length=50)
    assignment1 = models.CharField(max_length=50)