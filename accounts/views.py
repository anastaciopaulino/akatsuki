from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import OthersInfo
from accounts.forms import CreateUserForm, OthersInfoForm
from libs.gurls import gurls

from posts.models import PostImage

# Accounts views.py file
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()


class SignUp(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class UserOthersInfo(LoginRequiredMixin, generic.CreateView):
    form_class = OthersInfoForm
    template_name = 'accounts/others_info.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        if(self.object.sexo == 'Masculino'):
            self.object.avatar = 'accounts/images/avatar-m.jpg'
        else:
            self.object.avatar = 'accounts/images/avatar-f.jpg'           
        
        self.object.save()

        return super().form_valid(form)
    
class RedirectInfo(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # Controlando os outros dados
        if self.request.user.is_authenticated:
            if not OthersInfo.objects.filter(user_id=self.request.user.id).exists():
                return reverse('accounts:others-info', kwargs={
                    'username':self.request.user.username,
                    'token': str(gurls())
                })
        return reverse_lazy('index')

class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'accounts/authenticated/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['posts_recentes'] = PostImage.objects.filter(user__username=self.request.user.username)
        context['posts'] = PostImage.objects.filter(user__username=self.request.user.username)

        if context['posts_recentes'].count() > 8:
            context['posts_recentes'] = context['posts_recentes'][:8]

        return context