from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(name = "date", max_length = 15)
    title = models.CharField(name = "title", max_length = 35)
    content = models.CharField(name = "content", max_length = 250)
    post_image = models.ImageField(name = "postImage", upload_to = "postImages", null=True)
    location = models.CharField(name="location", max_length=50)

    def __str__(self):
        return f"{self.owner.first_name} {self.owner.last_name} ({self.title})"

class SocialPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(name = "age", null=True)
    status = models.CharField(name = "status", max_length = 70, default="Test")
    avatar = models.ImageField(name = "avatar", upload_to = "avatars")
    info = models.CharField(name = "info", max_length = 150, default="TEST")
    background_image = models.ImageField(name = "background", upload_to = "backs")
    jobs = models.CharField(name = "jobs", max_length = 150)
    add_info = models.CharField(name = "addInfo", max_length = 150, null=True)

    class Meta:
        verbose_name = "Social person"
        verbose_name_plural = "Social persons"

    def __str__(self):
        return f"""
            {self.user.first_name} {self.user.last_name} ({self.user.id})
        """
