import pytest

from ...serializers import TeamSerializer
from ..builders import BuilderModel


request_url = '/api/v1/team/'


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
def test_update_team_does_not_exist(client):
    """
    Check update method with team does not exist.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    json_team = {
        'user': (user.id + 1),
        'name': 'Betis FC'
    }

    url = request_url + str(user.id) + '/'

    response = client.put(url, data=json_team, content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_team_with_invalid_param(client):
    """
    Check update method with invalid param.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    json_team = {
        'user': user.id,
        'capacity_stadium': 'bad value',
        'expiration': '2222222',
    }

    url = request_url + str(user.id) + '/'

    response = client.put(url, data=json_team, content_type='application/json')

    assert response.status_code == 400
    

@pytest.mark.django_db
def test_update_team_with_invalid_date(client):
    """
    Check update method with invalid param.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    json_team = {
        'user': user.id,
        'expiration': '2222222',
    }

    url = request_url + str(user.id) + '/'

    response = client.put(url, data=json_team, content_type='application/json')

    assert response.status_code == 400
    
    
@pytest.mark.django_db
def test_update_team_with_invalid_capacity(client):
    """
    Check update method with invalid param.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    json_team = {
        'user': user.id,
        'capacity_stadium': 'bad value',
    }

    url = request_url + str(user.id) + '/'

    response = client.put(url, data=json_team, content_type='application/json')

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_team_with_invalid_plan_type(client):
    """
    Check update method with invalid param.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    json_team = {
        'user': user.id,
        'plan_type': 'PREMIUM',
    }

    url = request_url + str(user.id) + '/'

    response = client.put(url, data=json_team, content_type='application/json')

    assert response.status_code == 400
    
    
@pytest.mark.django_db
def test_update_team_with_invalid_matches_created(client):
    """
    Check update method with invalid param.
    """
    user = BuilderModel().build_user_test()
    BuilderModel().build_team_test(user)

    json_team = {
        'user': user.id,
        'matches_month_created': 1.11
    }

    url = request_url + str(user.id) + '/'

    response = client.put(url, data=json_team, content_type='application/json')

    assert response.status_code == 400