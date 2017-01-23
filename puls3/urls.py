"""puls3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoriaViewSet)
router.register(r'links', views.EnlaceViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^plus/(?P<enlace_id>\d+)/$', views.plus, name='plus'),
    url(r'^minus/(?P<enlace_id>\d+)/$', views.minus, name='minus'),
    url(r'^categoria/(?P<categoria_id>\d+)/$', views.categoria, name='categoria'),
    url(r'^add/$', views.add, name='add'),
    url(r'^about/$', TemplateView.as_view(template_name='index.html'), name='about'),
    url(r'^enlaces/$', views.EnlaceListView.as_view(), name='enlaces'),
    url(r'^enlace/(?P<pk>\d+)$', views.EnlaceDetailView.as_view(), name='enlace'),
]
