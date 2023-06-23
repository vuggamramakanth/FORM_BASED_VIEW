from django.db import models
from django import forms
# Create your models here.
from django.core import validators
def not_s_A(value):
    if value[0]=='a' or value[0]=='A':
        raise forms.ValidationError('it is started with a')


class Student(models.Model):
    sname=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(10),not_s_A])
    sid=models.IntegerField(primary_key=True)
    address=models.TextField()

    def __str__(self):
        return self.sname