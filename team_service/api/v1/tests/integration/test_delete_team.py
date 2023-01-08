import pytest

from ...models import Team
from ..builders import BuilderModel


request_url = '/api/v1/team/'


@pytest.mark.django_db
def test_delete_team(client):
    """
    Check delete method in team.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    url = request_url + str(user.id) + '/'
    response = client.delete(url, content_type='application/json')

    team_count = Team.objects.filter(user=user.id).count()

    assert response.status_code == 204
    assert team_count == 0


@pytest.mark.django_db
def test_delete_team_does_not_exist(client):
    """
    Verify that error is returned when trying 
    to delete a team that does not exist.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    url = request_url + str(user.id + 1) + '/'
    response = client.delete(url, content_type='application/json')

    team_count = Team.objects.filter(user=user.id).count()

    assert response.status_code == 404
    assert team_count == 1
