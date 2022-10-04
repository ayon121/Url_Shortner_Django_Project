from django.db import models
from hashlib import md5
# Create your models here.
class Url(models.Model):
    fullurl = models.CharField( unique=True ,max_length= 1000)
    shorturl = models.CharField ( unique=True ,max_length= 10)

    def __str__(self):
        return self.fullurl
    
    @classmethod
    def create(self , fullurl):
        temp_url = md5(fullurl.encode()).hexdigest()[:5] 
        try:
            obj = self.objects.create(fullurl=fullurl , shorturl = temp_url)
            
        except:
            obj = self.objects.get(fullurl = fullurl)
            
        return obj