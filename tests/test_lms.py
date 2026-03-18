import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from lms.models import Course, Lesson

User = get_user_model()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(
        email="test@test.com",
        password="12345"
    )


@pytest.fixture
def auth_client(client, user):
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def course(user):
    return Course.objects.create(
        title="Python",
        description="Programming",
        owner=user
    )


@pytest.fixture
def lesson(user, course):
    return Lesson.objects.create(
        title="Lesson 1",
        description="Intro",
        course=course,
        owner=user,
        video_url="https://www.youtube.com/watch?v=test"
    )


# ======================
# COURSE TESTS
# ======================

@pytest.mark.django_db
def test_create_course(auth_client):
    data = {
        "title": "Django",
        "description": "Backend framework"
    }

    response = auth_client.post("/api/courses/", data)

    assert response.status_code == 201
    assert Course.objects.count() == 1


@pytest.mark.django_db
def test_subscribe(auth_client, course):
    response = auth_client.post(
        "/api/subscribe/",
        {"course_id": course.id}
    )

    assert response.status_code == 200
    assert response.data["message"] == "подписка добавлена"


@pytest.mark.django_db
def test_unsubscribe(auth_client, course):
    auth_client.post(
        "/api/subscribe/",
        {"course_id": course.id}
    )

    response = auth_client.post(
        "/api/subscribe/",
        {"course_id": course.id}
    )

    assert response.data["message"] == "подписка удалена"


# ======================
# LESSON TESTS
# ======================

@pytest.mark.django_db
def test_create_lesson(auth_client, course):
    data = {
        "title": "Lesson 2",
        "description": "Basics",
        "video_url": "https://www.youtube.com/watch?v=test",
        "course": course.id
    }

    response = auth_client.post("/api/lessons/create/", data)

    assert response.status_code == 201
    assert Lesson.objects.count() == 1


@pytest.mark.django_db
def test_list_lessons(auth_client, lesson):
    response = auth_client.get("/api/lessons/")

    assert response.status_code == 200
    assert response.data["count"] == 1


@pytest.mark.django_db
def test_retrieve_lesson(auth_client, lesson):
    response = auth_client.get(f"/api/lessons/{lesson.id}/")

    assert response.status_code == 200
    assert response.data["title"] == lesson.title


@pytest.mark.django_db
def test_update_lesson(auth_client, lesson, course):
    data = {
        "title": "Updated lesson",
        "description": "New text",
        "video_url": "https://www.youtube.com/watch?v=test",
        "course": course.id
    }

    response = auth_client.put(
        f"/api/lessons/{lesson.id}/update/",
        data
    )

    assert response.status_code == 200

    lesson.refresh_from_db()
    assert lesson.title == "Updated lesson"


@pytest.mark.django_db
def test_delete_lesson(auth_client, lesson):
    response = auth_client.delete(
        f"/api/lessons/{lesson.id}/delete/"
    )

    assert response.status_code == 204
    assert Lesson.objects.count() == 0
