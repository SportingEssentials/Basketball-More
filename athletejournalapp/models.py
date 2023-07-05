from django.db import models

class Scent(models.Model):
    header = models.CharField(max_length=300, blank=True)
    player_name = models.CharField(max_length=200)
    colonge_name = models.CharField(max_length=200)
    colonge_image = models.ImageField(upload_to='images/', blank='True')
    colonge_url = models.URLField(max_length=1000)
    why = models.TextField(max_length=5000, blank=True)
    application = models.TextField(max_length=5000, blank=True)
    header_id = models.CharField(max_length=500, blank=True)

    player_image = models.ImageField(upload_to='images/', blank='True')

def formatted_description(self):
        return self.description.replace('\n', '<br>')






class BasketballEssential(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    coupons = models.CharField(max_length=200, blank=True)
    benefits = models.CharField(max_length=400, blank=True)
    stars = models.DecimalField(blank=True, max_digits=3, decimal_places=2)
    brand = models.CharField(max_length=200, blank=True)
    material = models.CharField(max_length=200, blank=True)
    url = models.URLField(max_length=200)
    sale = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=300, blank=True)







    def formatted_description(self):
        return self.description.replace('\n', '<br>')


    def __str__(self):
        return self.name


class Watch(models.Model):
     Name_player = models.CharField(max_length=400, blank=True)
     name_watch = models.CharField(max_length=400, blank=True)
     img_watch = models.ImageField(upload_to='images/', null=True)
     img_player = models.ImageField(upload_to='images/', null=True)
     description = models.TextField(max_length=10000, blank=True)



def formatted_description(self):
    return self.description.replace('\n', '<br>')