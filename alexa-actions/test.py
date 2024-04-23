import pytest

from alexa_actions import HomeAssistant, LaunchRequestHandler

from config import configuration

from const import (
    HA_URL,
    HA_TOKEN,
    SSL_VERIFY,
    DEBUG,
    AWS_DEFAULT_REGION,
)


@pytest.fixture
def config() -> None:
    """Function configuration."""
    configuration[HA_URL] = "http://localhost:8123"
    configuration[HA_TOKEN] = "bearerTest"
    configuration[SSL_VERIFY] = True
    configuration[DEBUG] = False
    configuration[AWS_DEFAULT_REGION] = "us-east-1"


@pytest.fixture
def home_assistant() -> HomeAssistant:
    """Function home_assistant."""
    return HomeAssistant(LaunchRequestHandler())


def test_ha_build_url(home_assistant: HomeAssistant) -> None:
    """Function test_ha_build_url."""
    url = home_assistant.get_ha_url()
    assert url == "http://localhost:8123/test"


def test_build_url(home_assistant) -> None:
    """Function test_build_url."""
    url = home_assistant._build_url("test")
    assert url == "http://localhost:8123/test"


def test_config_get(configuration) -> None:
    """Function test_config_get."""
    assert configuration[HA_URL] == "http://localhost:8123"
    assert configuration[HA_TOKEN] == "bearerTest"
    assert configuration[SSL_VERIFY] is True
    assert configuration[DEBUG] is False
    assert configuration[AWS_DEFAULT_REGION] == "us-east-1"
