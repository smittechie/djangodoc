from django.db import models


# Create your models here.
## Many to Many Relationship

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(models.Model):
    group = models.CharField(max_length=120)
    members = models.ManyToManyField(Person, through='Membership' , related_name='members')

    def __str__(self):
        return self.group


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
