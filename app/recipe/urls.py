from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
# router (I guess) generates extra urls for different actions for ViewSets
router.register('tags', views.TagViewSet)  # for recipe/tag

app_name = 'recipe'

urlpatterns = [
    # all urls from router are passed to tags because of ''
    path('', include(router.urls))
]
