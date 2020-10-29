from django import forms
from posts.models import PostImage

class PostImageForm(forms.ModelForm):
    class Meta():
        model = PostImage
        fields = ['title', 'image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = 'Titulo'

        self.fields['image'].label = 'Imagem'

        self.fields['description'].label = 'Descrição'