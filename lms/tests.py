from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Course

User = get_user_model()


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            password="12345"
        )

        self.course = Course.objects.create(
            title="Python",
            owner=self.user
        )

    def test_create_course(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "Django",
            "description": "Backend framework"
        }

        response = self.client.post("/api/courses/", data)

        self.assertEqual(response.status_code, 201)


    def test_subscribe(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post("/api/subscribe/", {
            "course_id": self.course.id
        })

        self.assertEqual(response.status_code, 200)
