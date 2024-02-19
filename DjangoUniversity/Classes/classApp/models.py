from django.db import models


class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=False, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=False, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    object = models.Manager()

    def __str__(self):
        display_course = '{0}: {1}'
        return display_course.format(self.title, self.instructor_name)

    class Meta:
        verbose_name_plural = "University Classes"
