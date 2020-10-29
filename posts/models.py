from django.db import models
from django.utils.text import slugify
from stdimage import StdImageField
from datetime import datetime

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

# Function to generate the image's file path
def image_directory_path(instance, filename):
    dt = datetime.now()

    filename = str(dt.strftime('IMG_%H%M%S%d%y%m')) + '.' + str(filename).split('.')[-1]
    return 'images/{0}/{1}' .format(instance.user.username, filename)

LIKE_CHOICES = {
    ('Like', 'Like'),
    ('UnLike', 'UnLike'),
}

class PostImage(models.Model):
    user = models.ForeignKey(User, related_name='userimage', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    title_url = models.CharField(editable=False, blank=True, max_length=50)
    
    image = StdImageField(upload_to=image_directory_path, 
                          variations={'large': (3840, 2160, True), 'thumbmnil': (400, 300, True)
    })

    quantity_like = models.ManyToManyField(User, related_name='quantity_like', default=None, blank=True)

    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return 'IMG_FROM_{}' .format(self.user.id)
    
    class Meta():
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.title_url = slugify(self.title)

        return super().save(*args, **kwargs)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(PostImage, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.user.id)

