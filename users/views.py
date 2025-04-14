from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from news.models import Article  # предполагается, что твоя модель статей — News


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['articles'] = Article.objects.filter(author=user).order_by('-publication_date')

        return context
