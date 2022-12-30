from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=40, blank=True,null=True)
    def __str__(self):
        return self.course_name

class Subject(models.Model):
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True, null=True)
    subject_name = models.CharField(max_length=40,blank=True,null=True)

    def __str__(self):
        return self.subject_name 


class Student(models.Model):
    course_enrolled = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    subject_chosen = models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=60,blank=True,null=True)
    dob = models.DateField()

    def __str__(self):
        return self.name