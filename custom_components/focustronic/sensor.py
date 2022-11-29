import logging

from homeassistant.helpers.entity import Entity
from homeassistant.helpers import device_registry as dr

from homeassistant import config_entries, core
from homeassistant.components.sensor import PLATFORM_SCHEMA
import voluptuous as vol

from homeassistant.helpers.entity import DeviceInfo

import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity

from homeassistant.helpers.typing import (
    ConfigType,
    DiscoveryInfoType,
    HomeAssistantType,
)

from typing import Any, Callable, Dict, Optional
import datetime

from .const import (
    DOMAIN,
    CONF_ACCESS_TOKEN
)

_LOGGER = logging.getLogger(__name__)


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_ACCESS_TOKEN): cv.string
    }
)


async def async_setup_entry(
    hass: core.HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities,
):

    """Setup sensors from a config entry created in the integrations UI."""
    api = hass.data[DOMAIN]["api"]
    config = hass.data[DOMAIN][config_entry.entry_id]
    dtsensors = [DosetronicSensor(dt, api) for dt in api["dosetronics"]]
    async_add_entities(dtsensors, update_before_add=True)
    dtpump1sensor = [DosetronicPump1Sensor(dt, api) for dt in api["dosetronics"]]
    async_add_entities(dtpump1sensor, update_before_add=True)
    dtpump2sensor = [DosetronicPump2Sensor(dt, api) for dt in api["dosetronics"]]
    async_add_entities(dtpump2sensor, update_before_add=True)
    dtpump3sensor = [DosetronicPump3Sensor(dt, api) for dt in api["dosetronics"]]
    async_add_entities(dtpump3sensor, update_before_add=True)
    dtpump4sensor = [DosetronicPump4Sensor(dt, api) for dt in api["dosetronics"]]
    async_add_entities(dtpump4sensor, update_before_add=True)
    dtpump5sensor = [DosetronicPump5Sensor(dt, api) for dt in api["dosetronics"]]
    async_add_entities(dtpump5sensor, update_before_add=True)

#    _LOGGER.debug("debug pump sensor create focustronic")
#    _LOGGER.debug(api)
#    for pump in 
#        dtpumpsensor = [DosetronicPump1ensor(dt, api) for dt in api["dosetronics"]]
#        async_add_entities(dtpump1sensor, update_before_add=True)
#    dtpumpsensors= [DosetronicPumpSensor(pump, api) for pump in api["dosetronics"]["pumps"]]
#    async_add_entities(dtpumpsensors, update_before_add=True)

#    for dt in api["dosetronics"]:
#        _LOGGER.debug("debug dt focustronic")
#        _LOGGER.debug(dt)
#        pumps = dt["settings"]["pumps"]
#        pumpsensors= [DosetronicPumpSensor(pump, api) for pump in pumps]
#        sync_add_entities(pumpsensor, update_before_add=True)




async def async_setup_platform(
    hass: HomeAssistantType,
    config: ConfigType,
    async_add_entities: Callable,
    discovery_info: Optional[DiscoveryInfoType] = None,
) -> None:
    """Set up the Nest climate device."""
    api = hass.data[DOMAIN]["api"]

    dosetronic_sensors = []
    _LOGGER.info("Adding dosetronic sensors")
    for sensor in api["dosetronics"]:
        _LOGGER.info(f"Adding dosetronic sensor name: {sensor}")
        dosetronic_sensors.append(DosetronicSensor(sensor, api))

    async_add_entities(dosetronic_sensors)

    dosetronic_pump1_sensors = []
    _LOGGER.info("Adding dosetronic pump sensors")
    for sensor in api["dosetronics"]:
        _LOGGER.info(f"Adding dosetronic pump sensor name: {sensor}")
        dosetronic_pump1_sensors.append(DosetronicPump1Sensor(sensor, api))

    async_add_entities(dosetronic_pump1_sensors)

    dosetronic_pump2_sensors = []
    _LOGGER.info("Adding dosetronic pump sensors")
    for sensor in api["dosetronics"]:
        _LOGGER.info(f"Adding dosetronic pump sensor name: {sensor}")
        dosetronic_pump2_sensors.append(DosetronicPump2Sensor(sensor, api))

    async_add_entities(dosetronic_pump2_sensors)

    dosetronic_pump3_sensors = []
    _LOGGER.info("Adding dosetronic pump sensors")
    for sensor in api["dosetronics"]:
        _LOGGER.info(f"Adding dosetronic pump sensor name: {sensor}")
        dosetronic_pump3_sensors.append(DosetronicPump3Sensor(sensor, api))

    async_add_entities(dosetronic_pump3_sensors)

    dosetronic_pump4_sensors = []
    _LOGGER.info("Adding dosetronic pump sensors")
    for sensor in api["dosetronics"]:
        _LOGGER.info(f"Adding dosetronic pump sensor name: {sensor}")
        dosetronic_pump4_sensors.append(DosetronicPump4Sensor(sensor, api))

    async_add_entities(dosetronic_pump4_sensors)

    dosetronic_pump5_sensors = []
    _LOGGER.info("Adding dosetronic pump sensors")
    for sensor in api["dosetronics"]:
        _LOGGER.info(f"Adding dosetronic pump sensor name: {sensor}")
        dosetronic_pump5_sensors.append(DosetronicPump5Sensor(sensor, api))

    async_add_entities(dosetronic_pump5_sensors)

class DosetronicSensor(Entity):

    def __init__(self, device_id, api):
        """Initialize the sensor."""
        self._name = "Dosetronic Sensor"
        self.device_id = device_id
        self.device = api

    @property
    def unique_id(self):
        """Return an unique ID."""
        return  self.device_id

    @property
    def state(self):
        """Return the state of the sensor."""
        try:
            if self.device.device_data[self.device_id]["is_active"] == 1:
            	return "Online"
            else:
            	return "Offline"
        except (IndexError, TypeError):
            return None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device.device_data[self.device_id]["friendly_name"]

    @property
    def extra_state_attributes(self):
        _LOGGER.debug(self.device.device_data[self.device_id])
        return {
            "friendly_name": self.device.device_data[self.device_id]["friendly_name"],
            "serial_number": self.device.device_data[self.device_id]["serial_number"],
            "firmware_version": self.device.device_data[self.device_id]["firmware_version"],
            "local_ip_address": self.device.device_data[self.device_id]["local_ip_address"],
            "is_active": self.device.device_data[self.device_id]["is_active"],
            "is_adv_active": self.device.device_data[self.device_id]["is_adv_active"],
            "last_online": datetime.datetime.fromtimestamp(self.device.device_data[self.device_id]["last_online"]).strftime('%c'),
        }
    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.device.device_data[self.device_id]["serial_number"])
            },
            name=self.device.device_data[self.device_id]["friendly_name"],
            manufacturer="Focustronic",
            model="Dosetronic",
            sw_version=self.device.device_data[self.device_id]["firmware_version"],
            hw_version=self.device.device_data[self.device_id]["serial_number"]
        )

    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()

class DosetronicPumpSensor(Entity):

    def __init__(self, device_id, api):
        """Initialize the sensor."""
        self._name = "Dosetronic Pump Sensor"
        self.device_id = device_id 
        self.device = api
#        self.device_pumps= 

    @property
    def unique_id(self):
        """Return an unique ID."""
        return  self.device_id +  "_pump_"

    @property
    def state(self):
        """Return the state of the sensor."""
        _LOGGER.info("debug pump 1 devicedata focustronic")
        _LOGGER.debug(self.device.device_data[self.device_id])
        try:
            return self.device.device_data[self.device_id]["settings"][0]["pump1_remaining_volume"] / 100
        except (IndexError, TypeError):
            return None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device_id + " Pump 1" 

    @property
    def extra_state_attributes(self):
        _LOGGER.debug(self.device.device_data[self.device_id])
        return {
            "unit_of_measurement": "mL",
            "friendly_name": self.device_id + self.device.device_data[self.device_id]["data"][0]["pump1"],
            "name": self.device.device_data[self.device_id]["data"][0]["pump1"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump1_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump1_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump1_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump1_remaining_volume"] / 100,
        }


    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()

class DosetronicPump1Sensor(Entity):

    def __init__(self, device_id, api):
        """Initialize the sensor."""
        self._name = "Dosetronic Pump Sensor"
        self.device_id = device_id 
        self.device = api

    @property
    def unique_id(self):
        """Return an unique ID."""
        return  self.device_id +  "_pump_1"

    @property
    def state(self):
        """Return the state of the sensor."""
        _LOGGER.info("debug pump 1 devicedata focustronic")
        _LOGGER.debug(self.device.device_data[self.device_id])
        try:
            return self.device.device_data[self.device_id]["data"][0]["pump1_remaining_volume"] / 100
        except (IndexError, TypeError):
            return None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device_id + " Pump 1" 

    @property
    def extra_state_attributes(self):
        _LOGGER.debug(self.device.device_data[self.device_id])
        return {
            "unit_of_measurement": "mL",
            "friendly_name": self.device_id + self.device.device_data[self.device_id]["data"][0]["pump1"],
            "name": self.device.device_data[self.device_id]["data"][0]["pump1"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump1_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump1_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump1_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump1_remaining_volume"] / 100,
        }
    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.device.device_data[self.device_id]["serial_number"])
            }
        )

    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()

class DosetronicPump2Sensor(Entity):

    def __init__(self, device_id, api):
        """Initialize the sensor."""
        self._name = "Dosetronic Pump Sensor"
        self.device_id = device_id 
        self.device = api

    @property
    def unique_id(self):
        """Return an unique ID."""
        return  self.device_id +  "_pump_2"

    @property
    def state(self):
        """Return the state of the sensor."""
        try:
            return self.device.device_data[self.device_id]["data"][0]["pump2_remaining_volume"] / 100
        except (IndexError, TypeError):
            return None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device_id + " Pump 2" 

    @property
    def extra_state_attributes(self):
        _LOGGER.debug(self.device.device_data[self.device_id])
        return {
            "unit_of_measurement": "mL",
            "name": self.device.device_data[self.device_id]["data"][0]["pump2"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump2_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump2_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump2_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump2_remaining_volume"] / 100,
        }
    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.device.device_data[self.device_id]["serial_number"])
            }
        )

    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()

class DosetronicPump3Sensor(Entity):

    def __init__(self, device_id, api):
        """Initialize the sensor."""
        self._name = "Dosetronic Pump Sensor"
        self.device_id = device_id 
        self.device = api

    @property
    def unique_id(self):
        """Return an unique ID."""
        return  self.device_id +  "_pump_3"

    @property
    def state(self):
        """Return the state of the sensor."""
        try:
            return self.device.device_data[self.device_id]["data"][0]["pump3_remaining_volume"] / 100
        except (IndexError, TypeError):
            return None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device_id + " Pump 3" 

    @property
    def extra_state_attributes(self):
        _LOGGER.debug(self.device.device_data[self.device_id])
        return {
            "unit_of_measurement": "mL",
            "name": self.device.device_data[self.device_id]["data"][0]["pump3"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump3_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump3_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump3_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump3_remaining_volume"] / 100,
        }
    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.device.device_data[self.device_id]["serial_number"])
            }
        )

    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()

class DosetronicPump4Sensor(Entity):

    def __init__(self, device_id, api):
        """Initialize the sensor."""
        self._name = "Dosetronic Pump Sensor"
        self.device_id = device_id 
        self.device = api

    @property
    def unique_id(self):
        """Return an unique ID."""
        return  self.device_id +  "_pump_4"

    @property
    def state(self):
        """Return the state of the sensor."""
        try:
            return self.device.device_data[self.device_id]["data"][0]["pump4_remaining_volume"] / 100
        except (IndexError, TypeError):
            return None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device_id + " Pump 4" 

    @property
    def extra_state_attributes(self):
        _LOGGER.debug(self.device.device_data[self.device_id])
        return {
            "unit_of_measurement": "mL",
            "name": self.device.device_data[self.device_id]["data"][0]["pump4"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump4_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump4_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump4_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump4_remaining_volume"] / 100,
        }
    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.device.device_data[self.device_id]["serial_number"])
            }
        )

    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()

class DosetronicPump5Sensor(Entity):

    def __init__(self, device_id, api):
        """Initialize the sensor."""
        self._name = "Dosetronic Pump Sensor"
        self.device_id = device_id 
        self.device = api

    @property
    def unique_id(self):
        """Return an unique ID."""
        return  self.device_id +  "_pump_5"

    @property
    def state(self):
        """Return the state of the sensor."""
        try:
            return self.device.device_data[self.device_id]["data"][0]["pump5_remaining_volume"] / 100
        except (IndexError, TypeError):
            return None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.device_id + " Pump 5" 

    @property
    def extra_state_attributes(self):
        _LOGGER.debug(self.device.device_data[self.device_id])
        return {
            "unit_of_measurement": "mL",
            "name": self.device.device_data[self.device_id]["data"][0]["pump5"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump5_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump5_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump5_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump5_remaining_volume"] / 100,
        }
    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.device.device_data[self.device_id]["serial_number"])
            }
        )

    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()
