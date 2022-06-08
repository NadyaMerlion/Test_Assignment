from django.db import models
import cmath


class Number(models.Model):
    a = models.IntegerField(null=False, default=0)
    b = models.IntegerField(null=False, default=0)
    c = models.IntegerField(null=False, default=0)
    result = models.CharField(max_length=20)


def __str__(self):
    return self.name


@property
def result(self):
    a = self.a
    b = self.b
    c = self.c
    discrement = (b**2) - (4 * a*c)
    result1 = (-b-cmath.sqrt(discrement))/(2 * a)
    result2 = (-b + cmath.sqrt(discrement))/(2 * a)
    result1.save()
    result2.save()
    return result1, result2
