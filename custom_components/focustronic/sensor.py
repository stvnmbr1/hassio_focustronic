import logging

from homeassistant.helpers.entity import Entity

import datetime

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
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
            "name": self.device.device_data[self.device_id]["data"][0]["pump2"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump2_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump2_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump2_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump2_remaining_volume"] / 100,
        }

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
            "name": self.device.device_data[self.device_id]["data"][0]["pump3"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump3_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump3_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump3_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump3_remaining_volume"] / 100,
        }

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
            "name": self.device.device_data[self.device_id]["data"][0]["pump4"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump4_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump4_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump4_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump4_remaining_volume"] / 100,
        }

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
            "name": self.device.device_data[self.device_id]["data"][0]["pump5"],
            "daily_volume": self.device.device_data[self.device_id]["data"][0]["pump5_daily_volume"] / 100,
            "last_24_hour_total_dose_volume": self.device.device_data[self.device_id]["data"][0]["pump5_last_24_hour_total_dose_volume"] / 100,
            "max_volume": self.device.device_data[self.device_id]["data"][0]["pump5_max_volume"] / 100,
            "remaining_volume": self.device.device_data[self.device_id]["data"][0]["pump5_remaining_volume"] / 100,
        }

    def update(self):
        """Get the latest data from the Protect and updates the states."""
        self.device.update()
