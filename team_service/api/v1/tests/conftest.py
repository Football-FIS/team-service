# -*- coding: utf-8 -*-
# -----------------------------------------------------------
# Test configuration
#
# Set initial data in DB test.
#
# email brunogllaga@icloud.com
# -----------------------------------------------------------

import pytest

from apps.api.models import Hotel, Room, Rate, Inventory


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    """
    Initialize data in the database.
    """
    with django_db_blocker.unblock():
        Hotel.objects.create(
            code="HT001",
            name="Meliá",
            country="ES",
            address="Calle Dr. Pedro de Castro, 1, Sevilla",
            zip_code=41004
        )
        assert set(h.code for h in Hotel.objects.all()) == {'HT001'}

        Room.objects.create(
            code="RM001",
            name="Deluxe",
            sleeps=4,
            facilities="Pool, air conditioning...",
            hotel=Hotel.objects.get(pk='HT001')
        )
        assert set(h.code for h in Room.objects.all()) == {'RM001'}

        Rate.objects.create(
            code="RT001",
            name="All-inclusive",
            room=Room.objects.get(pk='RM001')
        )
        assert set(h.code for h in Rate.objects.all()) == {'RT001'}

        Inventory.objects.create(
            date="2022-09-24",
            allotment=3,
            price=30.50,
            rate=Rate.objects.get(pk='RT001')
        )
        Inventory.objects.create(
            date="2022-09-25",
            allotment=3,
            price=30.50,
            rate=Rate.objects.get(pk='RT001')
        )
        Inventory.objects.create(
            date="2022-09-26",
            allotment=3,
            price=30.50,
            rate=Rate.objects.get(pk='RT001')
        )
        Inventory.objects.create(
            date="2022-09-27",
            allotment=3,
            price=30.50,
            rate=Rate.objects.get(pk='RT001')
        )
        assert set(str(h.date) for h in Inventory.objects.all()) == {'2022-09-24', '2022-09-25', '2022-09-26',
                                                                     '2022-09-27'}
