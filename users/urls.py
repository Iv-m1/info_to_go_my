from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.ProfileInfoView.as_view(), name='profile'),
    path('profile/articles/', views.UserArticlesView.as_view(), name='user_articles'),
    path('profile/activity/', views.ProfileActivityView.as_view(), name='profile_activity'),
]
