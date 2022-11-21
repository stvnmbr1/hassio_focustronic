"""The example integration."""
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

from .api import FocustronicAPI
from .const import (
    DOMAIN,
    CONF_ACCESS_TOKEN,
    CONF_UPDATE_TIMEOUT,
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.All(
            {
                vol.Required(CONF_ACCESS_TOKEN, default=""): cv.string,
            },
            {
                vol.Optional(CONF_UPDATE_TIMEOUT, default=15): cv.positive_int,
            },
        )
    },
    extra=vol.ALLOW_EXTRA,
)


def setup(hass, config):
    """Set up the focustronic component."""
    if config.get(DOMAIN) is not None:
        access_token = config[DOMAIN].get(CONF_ACCESS_TOKEN)
        update_timeout = config[DOMAIN].get(CONF_UPDATE_TIMEOUT)
    else:
        update_timeout = 120

    hass.data[DOMAIN] = {
        "api": FocustronicAPI(
            access_token,
            update_timeout,
        ),
    }

    return True
