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
    follows = models.ManyToManyField(User, blank=True)

    sexo = models.CharField(max_length=9, choices=SEXO_CHOICES)
    image = models.ImageField(upload_to=user_directory_path, blank=True, validators=[file_size_validator])
    avatar = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return 'user_{0}' .format(self.user.id)

    class Meta():
        ordering = ['-created_at']
    
class Follow(models.Model):
    user = models.OneToOneField(auth.get_user_model(),related_name='follows', on_delete=models.CASCADE)
    followUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '@{}' .format(self.user.id)
