from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class SocialPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(name = "age", null=True)
    status = models.CharField(name = "status", max_length = 70, default="Test")
    avatar = models.ImageField(name = "avatar", upload_to = "avatars")
    info = models.CharField(name = "info", max_length = 150, default="TEST")

    class Meta:
        verbose_name = "Social person"
        verbose_name_plural = "Social persons"

    def __str__(self):
        return f"""
            {this.user.first_name} {this.user.last_name} ({this.user.id})
        """
