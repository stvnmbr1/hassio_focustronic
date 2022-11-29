import logging

import requests
import time
import datetime


API_URL = "https://alkatronic.focustronic.com/api/v2/users/self/devices?token="
WEBAPI_BASE = "https://alkatronic.focustronic.com/api/v2/users/self/devices?token="
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/75.0.3770.100 Safari/537.36"
)


_LOGGER = logging.getLogger(__name__)


class FocustronicAPI:
    def __init__(
        self,
        access_token,
        update_timeout,
    ):
        self.device_data = {}
        self._wheres = {}
        self._access_token = access_token
        self.update_timeout = update_timeout
        self._session = requests.Session()
        self.dosetroncics = []
        self.dosetroncic_pumps = []
        self.devices = []
#        self.mastertronics = []
        self._get_devices()
        self.update()

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        return setattr(self, name, value)

    def __delitem__(self, name):
        return delattr(self, name)

    def __contains__(self, name):
        return hasattr(self, name)

    def _get_dosetronics(self, count=0):
        count += 1
        dosetronics = []

        try:
            r = self._session.get(
                f"https://alkatronic.focustronic.com/api/v2/users/self/devices?token={self._access_token}",
            )
            _LOGGER.debug(f"https://alkatronic.focustronic.com/api/v2/users/self/devices?token={self._access_token}")
            _LOGGER.debug(r.text)
            
            for dosetronic in r.json()["data"][1]["devices"]:
                dosetronics.append(dosetronic["friendly_name"])
                dosetronic["settings"]["pumps"] = list()
                self.device_data[dosetronic["friendly_name"]] = dosetronic

            _LOGGER.debug(f"Found {len(dosetronics)} dosetronics")

            return dosetronics
            
        except requests.exceptions.RequestException as e:
            _LOGGER.error(e)
            if count < 3:
                _LOGGER.error("RequestException : Failed to get dosetronics, trying again (max 3 attempts)")
                return self._get_dosetronics(count)

        except KeyError as e:
            if count < 3:
                _LOGGER.error(e)
                _LOGGER.debug(
                    "KeyError : Failed to get dosetronics, trying to log in again (max 3 attempts)"
                )
                return self._get_dosetronics(count)

    def _get_devices(self, count=0):
        count += 1
        try:
            self.dosetronics = self._get_dosetronics()

        except requests.exceptions.RequestException as e:
            _LOGGER.error(e)
            if count < 3:
                _LOGGER.error("Failed to get devices, trying again")
                return self._get_devices(count)
        except KeyError:
            if count < 3:
                _LOGGER.debug("Failed to get devices, trying to log in again")
                self.login()
                return self._get_devices(count)


    def update(self, count=0):
        count += 1

        try:
            # get dosetronics updates
            for dosetronic in self.dosetronics:
                r = self._session.get(
                    f"{WEBAPI_BASE}{self._access_token}",
                )
                if r.status_code == 200:
                    data = list()
                    data_to_process = r.json()["data"][1]["devices"]
                    for e in data_to_process:
                        data.append(
                            {
                                "friendly_name": e["friendly_name"],
                                "serial_number": e["serial_number"],
                                "firmware_version": e["firmware_version"],
                                "local_ip_address": e["local_ip_address"],
                                "is_active": e["is_active"],
                                "last_online": e["last_online"],
                                "is_adv_active": e["is_adv_active"],
                                "pumps":[
                                    {
                                    "name": e["settings"]["pumps"][0]["name"],
                                    "id": e["settings"]["pumps"][0]["id"],
                                    "remaining_volume": e["settings"]["pumps"][0]["remaining_volume"],
                                    "max_volume": e["settings"]["pumps"][0]["max_volume"],
                                    "daily_volume": e["settings"]["pumps"][0]["daily_volume"],
                                    "last_24_hour_total_dose_volume": e["settings"]["pumps"][0]["last_24_hour_total_dose_volume"],
                                    },
                                    {
                                    "name": e["settings"]["pumps"][1]["name"],
                                    "id": e["settings"]["pumps"][1]["id"],
                                    "remaining_volume": e["settings"]["pumps"][1]["remaining_volume"],
                                    "max_volume": e["settings"]["pumps"][1]["max_volume"],
                                    "daily_volume": e["settings"]["pumps"][1]["daily_volume"],
                                    "last_24_hour_total_dose_volume": e["settings"]["pumps"][1]["last_24_hour_total_dose_volume"],
                                    },
                                    {
                                    "name": e["settings"]["pumps"][2]["name"],
                                    "id": e["settings"]["pumps"][2]["id"],
                                    "remaining_volume": e["settings"]["pumps"][2]["remaining_volume"],
                                    "max_volume": e["settings"]["pumps"][2]["max_volume"],
                                    "daily_volume": e["settings"]["pumps"][2]["daily_volume"],
                                    "last_24_hour_total_dose_volume": e["settings"]["pumps"][2]["last_24_hour_total_dose_volume"],
                                    },
                                    {
                                    "name": e["settings"]["pumps"][3]["name"],
                                    "id": e["settings"]["pumps"][3]["id"],
                                    "remaining_volume": e["settings"]["pumps"][3]["remaining_volume"],
                                    "max_volume": e["settings"]["pumps"][3]["max_volume"],
                                    "daily_volume": e["settings"]["pumps"][3]["daily_volume"],
                                    "last_24_hour_total_dose_volume": e["settings"]["pumps"][3]["last_24_hour_total_dose_volume"],
                                    },
                                    {
                                    "name": e["settings"]["pumps"][4]["name"],
                                    "id": e["settings"]["pumps"][4]["id"],
                                    "remaining_volume": e["settings"]["pumps"][4]["remaining_volume"],
                                    "max_volume": e["settings"]["pumps"][4]["max_volume"],
                                    "daily_volume": e["settings"]["pumps"][4]["daily_volume"],
                                    "last_24_hour_total_dose_volume": e["settings"]["pumps"][4]["last_24_hour_total_dose_volume"],
                                    }
                                ],
                                "pump1": e["settings"]["pumps"][0]["name"],
                                "pump1_remaining_volume": e["settings"]["pumps"][0]["remaining_volume"],
                                "pump1_max_volume": e["settings"]["pumps"][0]["max_volume"],
                                "pump1_daily_volume": e["settings"]["pumps"][0]["daily_volume"],
                                "pump1_last_24_hour_total_dose_volume": e["settings"]["pumps"][0]["last_24_hour_total_dose_volume"],
                                "pump2": e["settings"]["pumps"][1]["name"],
                                "pump2_remaining_volume": e["settings"]["pumps"][1]["remaining_volume"],
                                "pump2_max_volume": e["settings"]["pumps"][1]["max_volume"],
                                "pump2_daily_volume": e["settings"]["pumps"][1]["daily_volume"],
                                "pump2_last_24_hour_total_dose_volume": e["settings"]["pumps"][1]["last_24_hour_total_dose_volume"],
                                "pump3": e["settings"]["pumps"][2]["name"],
                                "pump3_daily_volume": e["settings"]["pumps"][2]["daily_volume"],
                                "pump3_last_24_hour_total_dose_volume": e["settings"]["pumps"][2]["last_24_hour_total_dose_volume"],
                                "pump3_max_volume": e["settings"]["pumps"][2]["max_volume"],
                                "pump3_remaining_volume": e["settings"]["pumps"][2]["remaining_volume"],
                                "pump4": e["settings"]["pumps"][3]["name"],
                                "pump4_daily_volume": e["settings"]["pumps"][3]["daily_volume"],
                                "pump4_last_24_hour_total_dose_volume": e["settings"]["pumps"][3]["last_24_hour_total_dose_volume"],
                                "pump4_max_volume": e["settings"]["pumps"][3]["max_volume"],
                                "pump4_remaining_volume": e["settings"]["pumps"][3]["remaining_volume"],
                                "pump5": e["settings"]["pumps"][4]["name"],
                                "pump5_daily_volume": e["settings"]["pumps"][4]["daily_volume"],
                                "pump5_last_24_hour_total_dose_volume": e["settings"]["pumps"][4]["last_24_hour_total_dose_volume"],
                                "pump5_max_volume": e["settings"]["pumps"][4]["max_volume"],
                                "pump5_remaining_volume": e["settings"]["pumps"][4]["remaining_volume"],
                            }
                        )
                    _LOGGER.debug(f"Was able to get dosetronic data")
                    _LOGGER.debug(data)
                    self.device_data[dosetronic]["data"] = data
                else:
                    _LOGGER.error(f"Getting data failed")
                    self.device_data[dosetronic]["data"] = list()
        except (requests.exceptions.RequestException, ValueError,) as e:
            _LOGGER.error(e)
            if count < 3:
                _LOGGER.error("Failed to update, trying again")
                self.update(count)
        except KeyError:
            if count < 3:
                _LOGGER.error("Failed to update, trying to log in again")
                self.login()
                self.update(count)
