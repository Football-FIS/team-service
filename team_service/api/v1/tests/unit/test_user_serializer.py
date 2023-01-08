import pytest

from django.contrib.auth.models import User
from ...serializers import UserSerializer


def test_user_serializer():
    # GIVEN
    user = User(
        id=1,
        username="Username",
        first_name="FirstName",
        last_name="LastName",
        email="test@test.com"
    )

    # WHEN
    response = UserSerializer(user).data

    # THEN
    assert response == {
        'id': 1,
        'username': 'Username',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'email': 'test@test.com',
    }
