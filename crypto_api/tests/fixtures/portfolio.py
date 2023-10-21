from model_bakery import baker
import pytest

from crypto_api.models import Portfolio


@pytest.fixture()
def portfolio(user):
    return baker.make(
        Portfolio,
        user=user,
    )