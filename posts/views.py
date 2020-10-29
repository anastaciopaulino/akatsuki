from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.forms import PostImageForm
from posts.models import Like, PostImage

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()


class NewPhoto(LoginRequiredMixin, generic.CreateView):
    form_class = PostImageForm
    template_name = 'posts/new_post.html'

    def get_success_url(self):
        return reverse('accounts:user-detail', kwargs={
            'username': self.request.user.username,
            'pk': self.request.user.id
        })
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        self.object.save()
        return super().form_valid(form)

class LikePost(generic.RedirectView):
    def get_redirect_url(self):
        return reverse_lazy('index')
    
    def post(self, request, *args, **kwargs):
        user = request.user
        post_id = request.POST.get('post_id')
        post_obj = PostImage.objects.get(id=post_id)
        obj = Like.objects.filter(image_id=post_id, user=user)

        if user in post_obj.quantity_like.all():
            post_obj.quantity_like.remove(user)
        else:
            post_obj.quantity_like.add(user)
    
        if(obj.exists()):
            obj.delete()
        else:
            quantity_like, created = Like.objects.get_or_create(user=user, image_id=post_id)

            if not created:
                if quantity_like.value == 'Unlike':
                    quantity_like.value = 'Like'
                else:
                    quantity_like.value = 'Unlike'

            quantity_like.save()
        
        return super().post(request, *args, **kwargs)