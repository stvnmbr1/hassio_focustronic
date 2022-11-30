Focustronic integration for homeassistant

*WORK IN PROGRESS*
CODE CLEANUP ON THE TODOLIST


HACS installation available with GUI config
token still needed in configuration.yaml for now
please enter correct token in gui for future reference

only dosetronic available for now since i lack the hardware; for now

feel free to send me some jsons for other devices (without sensitive data eg. serialnumber)
PM me of you want to contribute


configuration.yml

focustronic:
 - access_token="TOKEN"
 
 
how to get token
use web developer tools and login to alkatronic website
search for the access token in response
