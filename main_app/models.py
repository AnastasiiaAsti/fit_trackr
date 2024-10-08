from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
from enum import Enum

# Create your models here.


class MuscleGroup(Enum):
    BICEPS = "Biceps"
    TRICEPS = "Triceps"
    CHEST = "Chest"
    BACK = "Back"
    LEGS = "Legs"
    ABS = "Abs"
    STRETCHING = "Stretching"
    LATS = "Lats"
    HAMSTRING = "Hamstring"
    CALVES = "Calves"
    QUADRICEPS = "Quadriceps"
    TRAPEZIUS = "Trapezius"
    SHOULDERS = "Shoulders"
    GLUTES = "Glutes"


class NewUser(AbstractUser):
    workout_goal = models.IntegerField(null=True, blank=True)
    calorie_goal = models.IntegerField(null=True, blank=True)
    def get_absolute_url(self):
        return reverse("user_dashboard")



class Day(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')

class Meal(models.Model):
    name = models.CharField()
    meal = models.CharField()
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    calories = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("user_dashboard")
    

class Workout(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    muscle_group = models.CharField(
        max_length=20,
        choices=[(key.name, key.value) for key in MuscleGroup],
        # default=MuscleGroup.BICEPS.value
    )
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    calorie_lost = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.muscle_group
    
    def get_absolute_url(self):
        return reverse("user_dashboard")

