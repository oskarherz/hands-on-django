from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

app_name = 'playground'

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='landing-page/'), name='index'),
    path('landing-page/', views.landing_page, name='landing-page'),
    path('posts/', views.posts, name='posts'),
    path('add-post/', views.add_post, name='add-posts'),
]
