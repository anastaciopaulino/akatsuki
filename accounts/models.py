from django.db import models
from django.contrib import auth
from datetime import datetime
from django.core.validators import ValidationError
# Create your models here.


def file_size_validator(value):
    limit = 1.6 * 1024 * 1024

    if value.size > limit:
        raise ValidationError('Arquivo muito grande! O tamanho não pode exceder 1.6 Mib')

# Function to generate the user's file path
def user_directory_path(instance, filename):
    dt = datetime.now()

    # File will be uploaded to MEDIA_ROOT/users/<id>/<filename>
    extension = str(filename).split('.')[-1]
    file_format = str(dt.strftime('IMG_%H%M%S%d%m%y.')) + extension

    return 'user/{0}/{1}'.format(instance.user.id, file_format)

class User(auth.models.User, auth.PermissionDenied):

    def __str__(self):
        return '@{}'.format(self.username)

SEXO_CHOICES = {
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')
}

class OthersInfo(models.Model):
    user = models.OneToOneField(auth.get_user_model(),related_name='others_info', on_delete=models.CASCADE)
    qtd_followers = models.ManyToManyField(User, blank=True, related_name='qtd_followers')
    qtd_following = models.ManyToManyField(User, blank=True , related_name='qtd_following')

    sexo = models.CharField(max_length=9, choices=SEXO_CHOICES)
    bio = models.TextField(max_length=160)
    
    image = models.ImageField(upload_to=user_directory_path, blank=True, validators=[file_size_validator])
    avatar = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return 'user_{0}' .format(self.user.id)

    class Meta():
        ordering = ['-created_at']
    
class Followers(models.Model):
    user = models.OneToOneField(auth.get_user_model(),related_name='followedUser', on_delete=models.CASCADE)
    followerUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '@{}' .format(self.user.id)

class Following(models.Model):
    user = models.OneToOneField(auth.get_user_model(), related_name='followingUser', on_delete=models.CASCADE)
    followingUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '@{}' .format(self.user.id)