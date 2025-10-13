from apps.courses.models import Evaluation

def get_evaluations_by_course(course_id):
    return Evaluation.objects.filter(course_id=course_id, active=True)
