"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from core import views
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'')
router.register(r'cliente', views.ClienteViewSet, basename='cliente')
router.register(r'hotel', views.HotelViewSet, basename='hotel')
router.register(r'voos', views.VooViewSet, basename='voo')
router.register(r'reserva', views.ReservaViewSet, basename='reserva')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('test_auth/', views.TestAuthView.as_view(), name='test_auth', ),
    path('rest-auth/logout/', views.LogoutViewEx.as_view(), name='rest_logout', ),
    path('rest-auth/login/', LoginView.as_view(), name='rest_login', ),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) -- https://docs.djangoproject.com/pt-br/3.0/howto/static-files/
