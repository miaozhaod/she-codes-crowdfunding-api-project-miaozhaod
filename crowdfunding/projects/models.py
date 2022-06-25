from django.db import models


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="pledges")
    supporter = models.CharField(max_length=200)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    goal = models.IntegerField()
    image = models.URLField()
    date_due = models.DateTimeField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)
