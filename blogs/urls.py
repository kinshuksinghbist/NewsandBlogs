from django.urls import path, include
from .views import BlogStandardView
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', BlogStandardView.as_view(), name='blogs' ),
    path('create/', views.create_blog, name='create_blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete_blog'),
]
