from django.db import models

from django.contrib.auth.models import User

class patientdata(models.Model):
    Age = models.FloatField()
    Sex = models.FloatField()
    Drug = models.FloatField()
    N_Days = models.FloatField()
    Ascites = models.FloatField()
    Spiders = models.FloatField()
    Hepatomegaly = models.FloatField()
    Edema = models.FloatField()
    Cholesterol = models.FloatField()
    Bilirubin = models.FloatField()
    Albumin = models.FloatField()
    Alk_Phos = models.FloatField()
    SGOT = models.FloatField()
    Tryglicerides = models.FloatField()
    Prothrombin = models.FloatField()
    Copper = models.FloatField()
    Platelets = models.FloatField()
    predicted_result = models.FloatField()

    def __str__(self):
        return f"Input for User {self.user.username} - Predicted Result: {self.predicted_result}"
    
    class Meta:
        app_label = 'myapp'
