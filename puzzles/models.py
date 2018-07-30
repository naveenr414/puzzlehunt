from django.db import models


class Puzzle(models.Model):
    number = models.IntegerField(default=0)
    answer = models.CharField(max_length=100)
    title = models.CharField(max_length=300)

    def __str__(self):
        return str(self.number)

class Submission(models.Model):
    team = models.ForeignKey("users.Team",on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    submitAnswer = models.CharField(max_length=100)
    result = models.BooleanField(default=False)


