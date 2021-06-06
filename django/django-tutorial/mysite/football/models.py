import datetime

from django.db import models
from django.utils import timezone


class Competitions(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=200,null=True)
    area_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @staticmethod
    def save_competition(name,code,area_name):
        """Method for saving competitions in the database"""
        try:
            Competitions(name=name, code=code, area_name=area_name).save()
            print( 'Success')
        except:
            print( 'Failure')


class Teams(models.Model):
    name = models.CharField(max_length=200, unique=True)
    tla = models.CharField(max_length=200, null=True)
    shortName = models.CharField(max_length=200)
    areaName = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    competition = models.ForeignKey(Competitions, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.name

    @staticmethod
    def save_team(name, tla, shortName, areaName, email):
        """Method for saving a team in the database"""
        try:
            Teams(name=name, tla=tla, shortName=shortName, areaName=areaName, email=email).save()
            print("Success")
        except:
            print("Failure")


class Players(models.Model):
    name = models.CharField(max_length=200, unique=True)
    position  = models.CharField(max_length=200)
    dateOfBirth  = models.CharField(max_length=200)
    countryOfBirth  = models.CharField(max_length=200)
    nationality  = models.CharField(max_length=200)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    @staticmethod
    def manage_info():
        """MEthod that will store the information requested"""