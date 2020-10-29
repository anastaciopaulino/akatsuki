from django.conf.urls import url
from accounts import views
from posts.views import NewPhoto
from django.contrib.auth import views as auth_views 

# App name
app_name = 'accounts'

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
    url(r'(?P<token>[-\w]+)/(?P<username>[-\w]+)/others-info/$', views.UserOthersInfo.as_view(), name='others-info'),
    url(r'check-info/$', views.RedirectInfo.as_view(), name='check-info'),
    url(r'(?P<username>[-\w]+)/(?P<pk>\d+)/detail/', views.UserDetailView.as_view(), name='user-detail'),
    url(r'(?P<username>[-\w]+)/(?P<pk>\d+)/new-photo', NewPhoto.as_view(), name='new-photo'),
]