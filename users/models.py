from django.db import models

# Create your models here.
class Team(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    grade = models.IntegerField(default=9)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name+" "+self.last_name
