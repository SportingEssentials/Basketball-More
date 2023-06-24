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
