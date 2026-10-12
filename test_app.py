import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home_returns_welcome_message(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["application"] == "ACEest Fitness & Gym"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_programs_endpoint(client):
    response = client.get("/programs")

    assert response.status_code == 200
    assert "fat_loss" in response.get_json()
    assert "muscle_gain" in response.get_json()
    assert "beginner" in response.get_json()


def test_calculate_calories_for_fat_loss(client):
    response = client.post(
        "/calculate-calories",
        json={"program": "fat_loss", "weight": 70},
    )

    assert response.status_code == 200
    assert response.get_json()["estimated_calories"] == 1540


def test_invalid_program_is_rejected(client):
    response = client.post(
        "/calculate-calories",
        json={"program": "unknown", "weight": 70},
    )

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_invalid_weight_is_rejected(client):
    response = client.post(
        "/calculate-calories",
        json={"program": "fat_loss", "weight": "seventy"},
    )

    assert response.status_code == 400
    assert "error" in response.get_json()
