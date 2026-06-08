"""Module containing JSON schemas for Restful-Booker API response validation."""

auth_schema = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}

booking_schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "totalprice": {"type": "number"},
        "depositpaid": {"type": "boolean"},
        "bookingdates": {
            "type": "object",
            "properties": {
                "checkin": {"type": "string"},
                "checkout": {"type": "string"}
            },
            "required": ["checkin", "checkout"]
        },
        "additionalneeds": {"type": "string"}
    },
    "required": ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]
}

booking_response_schema = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "number"},
        "booking": booking_schema
    },
    "required": ["bookingid", "booking"]
}
