"""domasna_193089 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FlowersApp.views import gardenForm, garden, home, gardenInfo, video, forum, reminder, flowerForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('garden/', garden, name="garden"),
    path('garden-form/', gardenForm, name="gardenForm"),
    path('home/', home, name="home"),
    path('garden-info/', gardenInfo, name="gardenInfo"),
    path('video/', video, name="video"),
    path('reminder/', reminder, name="reminder"),
    path('forum/', forum, name="forum"),
    path('flower-form/', flowerForm, name="flowerForm"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

