from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class PageImage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(name = "image", upload_to="pageImages")
    title = models.CharField(name = "title", max_length = 50)
    location = models.CharField(name = "location", max_length = 50)
    category = models.CharField(name = 'category', max_length = 35)

    def __str__(self):
        return f'{self.owner.first_name} {self.owner.last_name} ({self.title})'

class ImageFilter(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(name = "title", max_length=35)

    def __str__(self):
        return f'{self.owner.first_name} {self.owner.last_name} ({self.title})'


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(name="date", auto_now=True)
    title = models.CharField(name = "title", max_length = 35)
    content = models.CharField(name = "content", max_length = 250)
    post_image = models.ImageField(name = "postImage", upload_to = "postImages", null=True, blank=True)
    location = models.CharField(name="location", max_length=50)

    def __str__(self):
        return f"{self.owner.first_name} {self.owner.last_name} ({self.title})"

class SocialPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(name = "age", null=True)
    status = models.CharField(name = "status", max_length = 70, default="Test")
    avatar = models.ImageField(name = "avatar", upload_to = "avatars", blank=True)
    info = models.CharField(name = "info", max_length = 150, default="TEST")
    background_image = models.ImageField(name = "background", upload_to = "backs", blank=True)
    jobs = models.CharField(name = "jobs", max_length = 150)
    add_info = models.CharField(name = "addInfo", max_length = 150, null=True)
    friendsList = models.CharField(name = "friends", max_length=200, default="")

    class Meta:
        verbose_name = "Social person"
        verbose_name_plural = "Social persons"

    def __str__(self):
        return f"""
            {self.user.first_name} {self.user.last_name} ({self.user.id})
        """

class Comments(models.Model):
    pageOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    commentOwner = models.ForeignKey(SocialPerson, on_delete=models.CASCADE)
    text = models.CharField(name = "text", max_length=100, blank=True, default="")

    def __str__(self) :
        return f"Comment from {self.commentOwner.first_name} {self.pageOwner.first_name} ({self.text}) "