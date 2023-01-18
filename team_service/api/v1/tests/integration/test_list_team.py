import pytest

from ...models import Team
from ...serializers import TeamSerializer
from ..builders import BuilderModel


request_url = '/api/v1/team/'


@pytest.mark.django_db
def test_list_team(client):
    """
    Check list method in team.
    """
    user = BuilderModel().build_user_test()

    BuilderModel().build_team_test(user)

    response = client.get(request_url)

    teams = Team.objects.all()
    expected_data = TeamSerializer(teams, many=True).data
    response_data = response.data
    response_data[0]['user'] = None
    expected_data[0]['user'] = None

    assert response.status_code == 200
    assert str(response_data) == str(expected_data)
