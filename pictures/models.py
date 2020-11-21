from django.db import models
 
 
class Pictures(models.Model):
    name = models.CharField(max_length=255)
    culka = models.CharField(max_length=255)
 
    class Meta:
      verbose_name_plural = "pictures"
 
    def __str__(self):
        return self.name