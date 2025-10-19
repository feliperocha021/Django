from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EvaluationViewSet

router = DefaultRouter()
router.register(r'', CourseViewSet)
router.register(r'', EvaluationViewSet)

urlpatterns = router.urls
