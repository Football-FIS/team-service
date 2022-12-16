import pytest

from ..models import Team
from ..serializers import TeamSerializer
from .builders import BuilderModel


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

    assert response.status_code == 200
    assert response_data == expected_data


@pytest.mark.django_db
def test_create_team(client):
    """
    Check create method in hotels.
    """
    user = BuilderModel().build_user_test()
    json_team = {
        'user': user.id,
        'name': 'Sevilla FC',
        'country': 'Spain',
        'state': 'Sevilla',
        'city': 'Sevilla',
        'address': 'C. Sevilla Fútbol Club',
        'coach_name': 'Jorge Sampaoli',
        'stadium_name': 'Estadio Ramón Sánchez-Pizjuán',
        'capacity_stadium': 65000,
        'president_name': 'José Castro Carmona',
        'league_name': 'La Liga',
        'latitude': '75.021313',
        'longuitude': '56.021313',
        'plan_type': 'FRE',
    }

    response = client.post(request_url, data=json_team, format='json')

    expected_response = json_team
    expected_response['expiration'] = None
    response_dic = dict(response.data)

    assert response.status_code == 201
    assert response_dic == expected_response


@pytest.mark.django_db
def test_update_team(client):
    """
    Check update method in team.
    """
    user = BuilderModel().build_user_test()
    team = BuilderModel().build_team_test(user)

    json_team = {
        'user': user.id,
        'name': 'Betis FC'
    }

    url = request_url + str(user.id) + '/'

    response = client.put(url, data=json_team, content_type='application/json')

    response_dic = dict(response.data)
    expected_response = TeamSerializer(team).data
    expected_response['name'] = 'Betis FC'

    assert response.status_code == 200
    assert response_dic == expected_response


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
