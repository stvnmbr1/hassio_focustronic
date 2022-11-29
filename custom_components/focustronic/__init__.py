"""The example integration."""
import voluptuous as vol
from homeassistant.helpers import config_validation as cv
from homeassistant import config_entries, core
import logging

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

_LOGGER = logging.getLogger(__name__)

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

#def setup(hass: core.HomeAssistant, entry: config_entries.ConfigEntry):
#    """Set up the focustronic component."""
#    if hass.data.get(DOMAIN) is not None:
#        access_token = hass.data[DOMAIN][entry.entry_id].get(CONF_ACCESS_TOKEN)
#        _LOGGER.debug(f"init_data : setup{access_token}")
#
#    hass.data[DOMAIN] = {
#        "api": FocustronicAPI(
#            access_token,
#            update_timeout,
#        ),
#    }
#
#    return True


#def setup(
#    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
#) -> bool:
#
#    hass.data[DOMAIN][entry.entry_id][access_token] = access_token_1
#
#    _LOGGER.debug(f"hass_data : async_setup_entry{hass_data}")
#    
#    access_token = hass_data.get(access_token)
#
#    _LOGGER.debug(f"hass_data : async_setup_entry{access_token}")
#
#    hass.data[DOMAIN] = {
#        "api": FocustronicAPI(
#            access_token
#        ),
#    }
#
#    return True




#async def async_setup_entry(
#    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
#) -> bool:
#    """Set up platform from a ConfigEntry."""
#    if config.get(DOMAIN) is not None:
#        access_token = config[DOMAIN].get(CONF_ACCESS_TOKEN)
#        update_timeout = config[DOMAIN].get(CONF_UPDATE_TIMEOUT)
#    else:
#        update_timeout = 120
#
#    hass.data[DOMAIN] = {
#        "api": FocustronicAPI(
#            access_token,
#            update_timeout,
#        ),
#    }

    # Forward the setup to the sensor platform.
#    hass.async_create_task(
#        hass.config_entries.async_forward_entry_setup(entry, "sensor")
#    )
#    return True


#async def async_setup_entry(
#    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
#) -> bool:
#    """Set up platform from a ConfigEntry."""
#    hass.data.setdefault(DOMAIN, {})
#    hass.data[DOMAIN][entry.entry_id] = entry.data
#
#    _LOGGER.debug(f"data : async_setup_entry{entry.data}")
#
#    access_token=hass.data[DOMAIN][entry.entry_id].get(access_token)#
#
#    _LOGGER.debug(f"access_token : async_setup_entry{access_token}")
#
#    hass.data[DOMAIN] = {
#        "api": FocustronicAPI(
#            access_token
#        ),
#    }
#    # Forward the setup to the sensor platform.
#    hass.async_create_task(
#        hass.config_entries.async_forward_entry_setup(entry, "sensor")
#    )
#    return True


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Set up platform from a ConfigEntry."""
    hass.data.setdefault(DOMAIN, {})
    hass_data = dict(entry.data)
    hass.data[DOMAIN][entry.entry_id] = hass_data

    _LOGGER.debug(f"hass_data : async_setup_entry{hass_data}")
#    global access_token
#    access_token = hass_data.get(access_token)
#
#    _LOGGER.debug(f"hass_data : async_setup_entry{access_token}")
#
#    hass.data[DOMAIN] = {
#        "api": FocustronicAPI(
#            access_token
#        ),
#    }

    # Forward the setup to the sensor platform.
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True
