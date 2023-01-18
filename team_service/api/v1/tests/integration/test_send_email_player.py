import pytest


from ..builders import BuilderModel


request_url = '/api/v1/send-email-player'


@pytest.mark.django_db
def test_send_email_player(client):
    """
    Check integration with Player Service
    """
    team = BuilderModel().build_team_test(save=True)

    response = client.post(
        request_url,
        data={'user_id': team.user.id},
        format='json'
    )

    assert response.status_code == 202
