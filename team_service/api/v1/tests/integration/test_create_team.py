import pytest

from ..builders import BuilderModel


request_url = '/api/v1/team/'


@pytest.mark.django_db
def test_create_team(client):
    """
    Check create method in tean.
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
        'plan_type': 'PRE',
        'matches_month_created': 0
    }

    response = client.post(request_url, data=json_team, format='json')

    expected_response = json_team
    expected_response['expiration'] = None
    response_dic = dict(response.data)

    assert response.status_code == 201
    assert response_dic == expected_response


@pytest.mark.django_db
def test_create_team_without_required_param(client):
    """
    Check create method without required param.
    """
    json_team = {
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
        'plan_type': 'PRE',
        'matches_month_created': 0
    }

    response = client.post(request_url, data=json_team, format='json')

    expected_response = json_team
    expected_response['expiration'] = None

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_team_with_invalid_param(client):
    """
    Check create method with invalid param.
    """
    json_team = {
        'name': 'Sevilla FC',
        'country': 'Spain',
        'state': 'Sevilla',
        'city': 'Sevilla',
        'address': 'C. Sevilla Fútbol Club',
        'coach_name': 'Jorge Sampaoli',
        'stadium_name': 'Estadio Ramón Sánchez-Pizjuán',
        'capacity_stadium': '1',
        'president_name': 'José Castro Carmona',
        'league_name': 'La Liga',
        'latitude': '75.021313',
        'longuitude': '56.021313',
        'plan_type': 'POS',
        'matches_month_created': 0
    }

    response = client.post(request_url, data=json_team, format='json')

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_team_with_invalid_date(client):
    """
    Check create method with invalid param.
    """
    json_team = {
        'name': 'Sevilla FC',
        'country': 'Spain',
        'state': 'Sevilla',
        'city': 'Sevilla',
        'address': 'C. Sevilla Fútbol Club',
        'coach_name': 'Jorge Sampaoli',
        'stadium_name': 'Estadio Ramón Sánchez-Pizjuán',
        'capacity_stadium': 'bad value',
        'president_name': 'José Castro Carmona',
        'league_name': 'La Liga',
        'latitude': '75.021313',
        'longuitude': '56.021313',
        'plan_type': 'PRE',
        'expiration': '2222222',
        'matches_month_created': 0
    }

    response = client.post(request_url, data=json_team, format='json')

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_team_with_invalid_capacity(client):
    """
    Check create method with invalid param.
    """
    json_team = {
        'name': 'Sevilla FC',
        'country': 'Spain',
        'state': 'Sevilla',
        'city': 'Sevilla',
        'address': 'C. Sevilla Fútbol Club',
        'coach_name': 'Jorge Sampaoli',
        'stadium_name': 'Estadio Ramón Sánchez-Pizjuán',
        'capacity_stadium': 'bad value',
        'president_name': 'José Castro Carmona',
        'league_name': 'La Liga',
        'latitude': '75.021313',
        'longuitude': '56.021313',
        'plan_type': 'PRE',
        'expiration': '2222222',
        'matches_month_created': 0
    }

    response = client.post(request_url, data=json_team, format='json')

    assert response.status_code == 400
    

@pytest.mark.django_db
def test_create_team_with_invalid_plan_type(client):
    """
    Check create method with invalid param.
    """
    json_team = {
        'name': 'Sevilla FC',
        'country': 'Spain',
        'state': 'Sevilla',
        'city': 'Sevilla',
        'address': 'C. Sevilla Fútbol Club',
        'coach_name': 'Jorge Sampaoli',
        'stadium_name': 'Estadio Ramón Sánchez-Pizjuán',
        'capacity_stadium': 'bad value',
        'president_name': 'José Castro Carmona',
        'league_name': 'La Liga',
        'latitude': '75.021313',
        'longuitude': '56.021313',
        'plan_type': 'PREMIUM',
        'expiration': '2222222',
        'matches_month_created': 0
    }

    response = client.post(request_url, data=json_team, format='json')

    assert response.status_code == 400

   
@pytest.mark.django_db
def test_create_team_with_invalid_matches_created(client):
    """
    Check create method with invalid param.
    """
    json_team = {
        'name': 'Sevilla FC',
        'country': 'Spain',
        'state': 'Sevilla',
        'city': 'Sevilla',
        'address': 'C. Sevilla Fútbol Club',
        'coach_name': 'Jorge Sampaoli',
        'stadium_name': 'Estadio Ramón Sánchez-Pizjuán',
        'capacity_stadium': 'bad value',
        'president_name': 'José Castro Carmona',
        'league_name': 'La Liga',
        'latitude': '75.021313',
        'longuitude': '56.021313',
        'plan_type': 'PREMIUM',
        'expiration': '2222222',
        'matches_month_created': 1.11
    }

    response = client.post(request_url, data=json_team, format='json')

    assert response.status_code == 400
