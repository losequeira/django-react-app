from django.db import models

class Address(models.Model):
    state = models.CharField(
        'address state',
        max_length=200,
    )

    city = models.CharField(
        'address city',
        max_length=200,
    )

    zipcode = models.CharField(
        'zip code / postal code',
        max_length=12,
    )

    def __str__(self):
        return self.state + ', ' + self.city + ', ' + self.zipcode
    

class Student(models.Model):
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='the related address',
    )

    name = models.CharField(
        'student first name',
        max_length=250,
    )

    lastname = models.CharField(
        'student last name',
        max_length=250,
    )

    birthdate = models.DateTimeField('student birthdate')

    def __str__(self):
        return self.name + ' ' + self.lastname