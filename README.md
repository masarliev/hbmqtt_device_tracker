## Home Assistant device tracker for mqtt clients
Track connected devices to embedded brocker.
### Installation 
```sh
git clone https://github.com/masarliev/hbmqtt_device_tracker.git
cd hbmqtt_device_tracker
source /path/to/virtualenv
pip3 install .
```
### HASS config
```yaml
# Setup as device
device_tracker:
  - platform: mqtt
    devices:
      nodemcu: "location/client_id"
      esp8266: "location/eps_client_id"
 
 # Setup as binary sensor
 binary_sensor:
  - platform: mqtt
    name: Nodemcu
    state_topic: "location/client_id"
    payload_on: "home"
    payload_off: "not_home"
```
