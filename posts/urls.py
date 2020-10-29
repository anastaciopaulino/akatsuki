from django.urls import path
from posts import views

# APP NAME
app_name = 'posts'

urlpatterns = [
    path('<slug:title>/like/', views.LikePost.as_view(), name='post-like'),
]