import pytest

import requests
from ..builders import BuilderModel


request_url = 'https://player-service-danaremar.cloud.okteto.net/api/v1/notify-players'


@pytest.mark.django_db
def test_send_email_player(client):
    """
    Check integration with Player Service
    """
    response = requests.post(
        request_url,
        json={
            "alignment": "string",
            "city": "string",
            "id": "string",
            "is_local": True,
            "opponent": "string",
            "sent_email": True,
            "start_date": "string",
            "url": "string",
            "user_id": 0,
            "weather": "string"
        }
    )
    assert response.status_code == 202


@pytest.mark.django_db
def test_send_email_player_bad_param(client):
    """
    Check integration with Player Service
    """
    response = requests.post(
        request_url,
        json={
            "alignment": "string",
            "city": "string",
            "id": "string",
            "is_local": True,
            "opponent": "string",
            "sent_email": 123,
            "start_date": "string",
            "url": "string",
            "user_id": 0,
            "weather": "string"
        }
    )
    assert response.status_code == 400
