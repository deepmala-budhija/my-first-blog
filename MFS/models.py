from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class MFS(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    survey_date = models.DateTimeField(default=timezone.now)

    BHOOTGARH = 'Bhootgarh'
    MAJRA = 'Majra'
   
    VILLAGE_CHOICES = [
        (BHOOTGARH, 'Bhootgarh'),
        (MAJRA, 'Majra'),
    ]
    village = models.CharField( max_length=100,choices=VILLAGE_CHOICES, )
    
    name_of_surveyor = models.CharField(max_length=500)
    house_number = models.IntegerField(validators=[MinValueValidator(1)])
    household_number = models.TextField()

    def __str__(self):
        return self.house_number





