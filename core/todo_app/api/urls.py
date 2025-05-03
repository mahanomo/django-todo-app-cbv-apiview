from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TodoTaskModelViewSet)
# router.register('tasks/<int:pk>', views.TodoTaskModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    ]