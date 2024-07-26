from django.urls import path
from rest_framework.routers import DefaultRouter

# from .views import BookReviewDetailAPIView, BookReviewsAPIView
from api.views import BookReviewsViewSet

app_name = "api"

router = DefaultRouter()
router.register('reviews', BookReviewsViewSet, basename='review')

urlpatterns = router.urls
