from django.db import models

# Create your models here.
from django.db import models

import re
from django.utils import timezone

class Person(models.Model):
    line = 0
    lineNumber = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    phoneNumber = models.IntegerField()
    service = models.IntegerField()
    waitTime = models.IntegerField()

    def __str__(self):
        return self.firstName + "\t" + self.lastName + "\t" + str(self.phoneNumber) + "\t" + str(self.service)

    def getLineNumber(self):
        obj = Person.objects.all()

        self.line = obj[len(obj)-1].lineNumber
        self.line += 1
        return self.line

    def minuteMinder(self):
        obj = Person.objects.all()
        return obj[len(obj)-1].service + obj[len(obj)-1].waitTime


