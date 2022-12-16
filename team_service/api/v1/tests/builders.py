import pytest

from django.contrib.auth.models import User

from api.v1.models import Team


@pytest.mark.django_db
class BuilderModel(object):
    def build_user_test(self):
        """
        Create user test
        """
        user = User.objects.create_user(
            username='test',
            password='pbkdf2_sha256$390000$ijaFVitO0ONCG430Z1Xh' +
                     'kA$/0RsQolIHYpVEeogMpcn5cqnhg0Yj6EjycMpqqpe+rQ='
        )

        return user

    def build_team_test(self, user=None):
        """
        Create team test
        """
        if not user:
            user = self.build_user_test()

        team = Team.objects.create(
            user=user,
            name='Sevilla FC',
            country='Spain',
            state='Sevilla',
            city='Sevilla',
            address='C. Sevilla Fútbol Club',
            coach_name='Jorge Sampaoli',
            stadium_name='Estadio Ramón Sánchez-Pizjuán',
            capacity_stadium=65000,
            president_name='José Castro Carmona',
            league_name='La Liga',
            latitude='75.021313',
            longuitude='56.85283',
            expiration=None,
            plan_type='FRE',
        )

        return team
