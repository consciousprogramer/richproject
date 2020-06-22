from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


# Create your models here.
class usermessage(models.Model):
    fname = models.CharField(max_length = 100)
    email = models.CharField(max_length=255)
    message = models.TextField()
    mob_no = models.IntegerField()
    def __str__(self):
        return f"{self.fname}__ message is__{self.message}!"


class patient(models.Model):
    # raw_json_data = JSONField()
    gender = models.CharField(max_length = 10)
    hair_color = models.CharField(max_length = 25)
    baldness_pattern = models.CharField(max_length = 50)
    had_transplant = models.CharField(max_length = 30)
    problem_since = models.CharField(max_length = 20)
    how_bad = models.CharField(max_length = 50)
    urgency = models.CharField(max_length = 60)
    fullname = models.CharField(max_length = 80)
    age = models.IntegerField()
    email =models.CharField(max_length=255,unique=True)
    mob_no = models.CharField(max_length = 11)
    profile_image = models.ImageField(upload_to='media/images', default="")


    def __str__(self):
        return f"{self.fullname}__{self.mob_no}__{self.email}"

class add_offer(models.Model):
    is_active = models.BooleanField(default = False)
    background_color = models.CharField(max_length = 30)
    background_image = models.ImageField(upload_to='media/images', default="")
    offer_age = models.IntegerField()
    font_family = models.CharField(max_length = 40)
    title = models.CharField(max_length = 150)
    is_right_header = models.BooleanField(default = False)
    right_header = models.CharField(max_length = 100)
    is_left_header = models.BooleanField(default = False)
    left_header = models.CharField(max_length = 100)
    is_right_content = models.BooleanField(default = False)
    right_content = models.TextField()
    is_left_content = models.BooleanField(default = False)
    left_content = models.TextField()
    offer_button_color = models.CharField(max_length = 10)
    offer_button_innertext = models.CharField(max_length = 30)


    def __str__(self):
        return f"offer: {self.title}__run for__{self.offer_age} days."
