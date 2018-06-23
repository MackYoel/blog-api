from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'posts'

router = DefaultRouter()
router.register('posts', views.PostViewSet, base_name='api_posts')

urlpatterns = router.urls + []
