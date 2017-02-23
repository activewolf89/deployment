from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length = 45)
    course_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.course_name
