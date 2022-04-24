from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'posts', views.PostAPIView)
router.register(r'comments', views.CommentAPIView)

urlpatterns = [
    path('', include(router.urls))
]
