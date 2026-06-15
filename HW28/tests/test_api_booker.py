"""Module containing API integration tests for the Restful-Booker service."""

import pytest
import requests
from jsonschema import validate

from HW28.schemas import auth_schema, booking_response_schema, booking_schema
from logger_config import get_logger

logger = get_logger("test_api_booker")
BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session", name="auth_token")
def fixture_auth_token():
    payload = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", json=payload, timeout=10)
    assert response.status_code == 200
    return response.json().get("token")


@pytest.fixture(name="new_booking")
def fixture_new_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-06-01", "checkout": "2026-06-10"},
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload, timeout=10)
    assert response.status_code == 200
    return response.json()


# Positive test

def test_create_token_success():
    logger.info("Starting test: Create Token Validation")
    payload = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", json=payload, timeout=10)

    assert response.status_code == 200
    validate(instance=response.json(), schema=auth_schema)
    logger.info("Token schema successfully validated")


def test_create_booking_success(new_booking):
    logger.info("Starting test: Create Booking Validation")
    validate(instance=new_booking, schema=booking_response_schema)
    assert new_booking["booking"]["firstname"] == "Jim"
    logger.info("Booking payload and schema validated successfully")


def test_get_booking_success(new_booking):
    booking_id = new_booking["bookingid"]
    logger.info("Starting test: Get Booking by ID %s", booking_id)

    response = requests.get(f"{BASE_URL}/booking/{booking_id}", timeout=10)
    assert response.status_code == 200
    validate(instance=response.json(), schema=booking_schema)
    logger.info("Booking details fetched and verified")


def test_get_all_bookings_success():
    logger.info("Starting test: Get All Bookings")
    response = requests.get(f"{BASE_URL}/booking", timeout=10)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_booking_success(new_booking, auth_token):
    booking_id = new_booking["bookingid"]
    logger.info("Starting test: Full Update Booking %s", booking_id)

    headers = {"Accept": "application/json", "Cookie": f"token={auth_token}"}
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-06-01", "checkout": "2026-06-10"},
        "additionalneeds": "Dinner"
    }
    response = requests.put(
        f"{BASE_URL}/booking/{booking_id}", json=payload, headers=headers, timeout=10
    )
    assert response.status_code == 200
    validate(instance=response.json(), schema=booking_schema)
    assert response.json()["firstname"] == "James"


def test_partial_update_booking_success(new_booking, auth_token):
    booking_id = new_booking["bookingid"]
    logger.info("Starting test: Partial Update Booking %s", booking_id)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    payload = {"firstname": "Johnny", "totalprice": 250}
    response = requests.patch(
        f"{BASE_URL}/booking/{booking_id}", json=payload, headers=headers, timeout=10
    )
    assert response.status_code == 200
    validate(instance=response.json(), schema=booking_schema)
    assert response.json()["firstname"] == "Johnny"


def test_delete_booking_success(new_booking, auth_token):
    booking_id = new_booking["bookingid"]
    logger.info("Starting test: Delete Booking %s", booking_id)

    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers, timeout=10)
    assert response.status_code == 201


# Negative tests

def test_get_non_existent_booking_error():
    invalid_id = 99999999
    response = requests.get(f"{BASE_URL}/booking/{invalid_id}", timeout=10)
    assert response.status_code == 404


def test_delete_non_existent_booking_error(auth_token):
    headers = {"Cookie": f"token={auth_token}"}
    invalid_id = 99999999
    response = requests.delete(f"{BASE_URL}/booking/{invalid_id}", headers=headers, timeout=10)
    assert response.status_code == 405
