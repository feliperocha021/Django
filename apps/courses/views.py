from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer
from .services import get_evaluations_by_course

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def evaluations(self, request, pk=None):
        evaluations = get_evaluations_by_course(pk)
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
