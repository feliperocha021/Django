from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Base(models.Model):
  creation = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True) 

  class Meta:
    abstract = True

class Course(Base):
  title = models.CharField(max_length=255)
  url = models.URLField(unique=True)

  class Meta:
    verbose_name = 'Course'
    verbose_name_plural = "Courses"
    ordering = ['-creation']

  def __str__(self):
    return self.title

class Evaluation(Base):
  course = models.ForeignKey(Course, related_name="evaluations", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  comments = models.TextField(blank=True, default="")
  grade = models.DecimalField(max_digits=3, decimal_places=1, validators=[
    MinValueValidator(0), MaxValueValidator(10)
  ])

  class Meta:
    verbose_name = "Evaluation"
    verbose_name_plural = "Evaluations"
    constraints = [
        models.UniqueConstraint(fields=['email', 'course'], name='unique_evaluation_per_course')
    ]
    ordering = ['-creation']
  
  def __str__(self):
    return f'{self.name} grade the course {self.course} with a grade {self.grade}'
