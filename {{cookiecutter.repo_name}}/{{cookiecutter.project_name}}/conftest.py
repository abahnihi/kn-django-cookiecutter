import pytest

from {{ cookiecutter.project_name }}.user.models import User
from {{ cookiecutter.project_name }}.user.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()
