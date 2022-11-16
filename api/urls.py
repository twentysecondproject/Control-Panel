from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'people', views.showallpeople)
router.register(r'comments', views.showallcomments)


urlpatterns = [
    path('', include(router.urls))
]