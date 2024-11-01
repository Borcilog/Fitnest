from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
 
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/%y')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def str(self):
        return self.name
