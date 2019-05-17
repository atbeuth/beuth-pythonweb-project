from django.db import models


# Create your models here.
class Post(models.Model):
    #firstname = models.TextField(max_length=50)
    #lastname = models.TextField(max_length=50)
    image_url = models.ImageField(upload_to ='media/', default = 'media/no-img.jpg')
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()


    def summary(self):
        return self.content + ': ' + self.content

    def __str__(self):
        return self.content + ' +' + str(self.upvotes)
        + ' -' + str(self.downvotes)
