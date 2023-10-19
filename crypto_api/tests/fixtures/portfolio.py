from model_bakery import baker
import pytest

from crypto_api.models import Portfolio


@pytest.fixture()
def company():
    return baker.make(Portfolio)