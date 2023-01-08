import pytest

from ...serializers import TeamSerializer
from ..builders import BuilderModel


def test_team_serializer():
    # GIVEN
    user = BuilderModel().build_user_test(save=False)
    team = BuilderModel().build_team_test(user, save=False)

    # WHEN
    response = TeamSerializer(team).data

    # THEN
    assert response == {
        'address': 'C. Sevilla Fútbol Club',
        'capacity_stadium': 65000,
        'city': 'Sevilla',
        'coach_name': 'Jorge Sampaoli',
        'country': 'Spain',
        'expiration': None,
        'latitude': '75.021313',
        'league_name': 'La Liga',
        'longuitude': '56.85283',
        'matches_month_created': 0,
        'name': 'Sevilla FC',
        'plan_type': 'FRE',
        'president_name': 'José Castro Carmona',
        'stadium_name': 'Estadio Ramón Sánchez-Pizjuán',
        'state': 'Sevilla',
        'user': None
    }
