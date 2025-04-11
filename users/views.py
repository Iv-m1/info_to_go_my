from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from news.models import Article  # Замените на вашу модель новостей

class ProfileBaseView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['profile'] = user.profile
        return context

class ProfileInfoView(ProfileBaseView):
    template_name = 'users/profile_info.html'

class UserArticlesView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'users/profile_articles.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('publication_date')

class ProfileActivityView(ProfileBaseView):
    template_name = 'users/profile_activity.html'
