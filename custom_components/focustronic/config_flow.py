import secrets
import logging
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_ACCESS_TOKEN
from .const import (
    DOMAIN#,
#    CONF_ACCESS_TOKEN,
#    CONF_UPDATE_TIMEOUT,
)
#from homeassistant.const import CONF_ACCESS_TOKEN
from typing import Any, Dict, Optional
from homeassistant import config_entries, core
from homeassistant.helpers.entity_registry import (
    async_entries_for_config_entry,
    async_get_registry,
)
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

AUTH_SCHEMA = vol.Schema(
    {vol.Required(CONF_ACCESS_TOKEN): cv.string}
)

class FocustronicConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    data: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Invoked when a user initiates a flow via the user interface."""
#        errors: Dict[str, str] = {}
        if user_input is not None:
#            try:
#                await validate_auth(user_input[CONF_ACCESS_TOKEN], self.hass)
#            except ValueError:
#                errors["base"] = "auth"
#            if not errors:
#                # Input is valid, set data.
#                self.data = user_input
            self.data = user_input

            return self.async_create_entry(title="Focustronic", data=self.data)

        return self.async_show_form(
            step_id="user", data_schema=AUTH_SCHEMA#, errors=errors
        )
