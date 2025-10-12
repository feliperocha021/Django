from django.contrib import admin
from .models import Course, Evaluation

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'creation', 'update', 'active')
    search_fields = ('title', 'url')
    list_filter = ('active', 'creation')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'email', 'grade', 'creation', 'update', 'active')
    search_fields = ('name', 'email')
    list_filter = ('course', 'grade', 'active')
