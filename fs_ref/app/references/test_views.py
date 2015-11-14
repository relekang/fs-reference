# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
import pytest as pytest


@pytest.mark.django_db
def test_topics_with_no_query(admin_client):
    response = admin_client.get(reverse('all_references'))
    assert response.status_code == 200

