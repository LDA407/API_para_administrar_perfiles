from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from profiles_api import views
router = DefaultRouter()


router.register('viewset', views.HelloViewSet, basename='viewset')
router.register('profile', views.UserProfilViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('helloapiview/', views.HelloApiView.as_view(), name='helloapiview'),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]