from django.db import models

# Create your models here.
class Post(models.Model):
    #image_url = models.ImageField(upload_to ='media/', default = 'media/assets/no_pic.png')
    image_url = models.ImageField(upload_to ='media/', null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,  null=True)  #TextField(max_length=5, default = "")
    content = models.TextField(max_length=1000)
    tags = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)


    def summary(self):
        return self.content + ': ' + self.content

    def __str__(self):
        return self.content + ' +' + str(self.upvotes) + ' -' + str(self.downvotes)
