from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EvaluationViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'evaluations', EvaluationViewSet)

urlpatterns = router.urls
