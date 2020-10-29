from django.views import generic
from posts.models import PostImage

class HomePage(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['posts_recentes'] = PostImage.objects.all()[:9]

        return context
