"""djangoExample URL Configuration

The `urlpatterns` list routes URLs to playground. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function playground
    1. Add an import:  from my_app import playground
    2. Add a URL to urlpatterns:  path('', playground.home, name='home')
Class-based playground
    1. Add an import:  from other_app.playground import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/playground/'), name='index'),
    path('playground/', include('djangoExample.playground.urls', namespace='playground')),
    path('admin/', admin.site.urls),
]

