from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from gamerraterapi.views import register_user, login_user
from rest_framework import routers
from gamerraterapi.views import GameView, CategoryView, RatingView, ReviewView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'games', GameView, 'game')
router.register(r'categories', CategoryView, 'category')
router.register(r'ratings', RatingView, 'rating')
router.register(r'reviews', ReviewView, 'review')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),     
    path('', include('gamerraterreports.urls')),
]
