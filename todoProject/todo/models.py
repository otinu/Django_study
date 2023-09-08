from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = CHOICE
    )
    duedate = models.DateField()

    def __str__(self):
        return slf.title