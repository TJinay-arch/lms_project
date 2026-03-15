from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)

    preview = models.ImageField(upload_to="courses/previews/", blank=True, null=True)

    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["id"]


class Lesson(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    preview = models.ImageField(upload_to="lessons/previews/", blank=True, null=True)

    video_url = models.URLField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"