from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    SubscriptionAPIView,
)

router = DefaultRouter()
router.register("courses", CourseViewSet)

urlpatterns = router.urls

urlpatterns += [
    path("lessons/", LessonListAPIView.as_view()),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view()),
    path("lessons/create/", LessonCreateAPIView.as_view()),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view()),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view()),
    path("subscribe/", SubscriptionAPIView.as_view()),
]
