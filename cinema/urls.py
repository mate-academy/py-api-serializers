# write urls here
from django.urls import path, include

app_name = 'cinema'
from rest_framework import routers
from cinema import views

router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]