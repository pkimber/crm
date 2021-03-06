# -*- encoding: utf-8 -*-
import pytest

from datetime import timedelta

from django.utils import timezone

from crm.tests.factories import NoteFactory
from search.tests.helper import check_search_methods


@pytest.mark.django_db
def test_search_methods():
    check_search_methods(NoteFactory())


@pytest.mark.django_db
def test_str():
    str(NoteFactory())


@pytest.mark.django_db
def test_modified_today():
    assert NoteFactory().modified_today() is True


@pytest.mark.django_db
def test_modified_tomorrow():
    tomorrow = timezone.now() + timedelta(days=1)
    obj = NoteFactory()
    obj.created = tomorrow
    obj.save()
    assert obj.modified_today() is False


@pytest.mark.django_db
def test_modified_yesterday():
    yesterday = timezone.now() - timedelta(days=1)
    obj = NoteFactory()
    obj.created = yesterday
    obj.save()
    assert obj.modified_today() is False
