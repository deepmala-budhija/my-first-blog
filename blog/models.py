from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class LineListing(models.Model):
   
        survey_date = models.DateField()
        VILLAGE_CHOICES = [
            ('Boothgarh', 'Boothgarh'),
            ('Majra', 'Majra'),
            ('Pallanpur','Pallanpur'),
            ('Khijrabad','Khijrabad'),
            ('Manakpur sharif','Manakpur sharif'),
            ('Sangatpura','Sangatpura'),
            ('Abhipur','Abhipur'),
            ('Fatwan','Fatwan'),
            ('Thakoran kalan','Thakoran kalan')  ,         
        ]
        village = models.CharField( max_length=100,choices=VILLAGE_CHOICES, ) 
        
        person_name_collecting_data = models.CharField(max_length=500)
        house_number = models.PositiveIntegerField()
        household_number = models.CharField(max_length=1)

        def submit_survey(self):
            self.save()

        def __str__(self):
            return self.house_number






