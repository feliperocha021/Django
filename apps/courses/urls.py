from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EvaluationViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'evaluations', EvaluationViewSet, basename='evaluation')

urlpatterns = router.urls
