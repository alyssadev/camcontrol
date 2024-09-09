camcontrol
==========

A project to expose v4l2-ctl configuration to home assistant on my lan. Runs on the camera-operating system (pi 4 in my case)

Home Assistant config
---------------------

```
rest_command:
  cam_exposure_up:
    url: "http://cam.local:5000/exposure_time_absolute/up"
    method: get
  cam_exposure_down:
    url: "http://cam.local:5000/exposure_time_absolute/down"
    method: get
  cam_focus_up:
    url: "http://cam.local:5000/focus_absolute/up"
    method: get
  cam_focus_down:
    url: "http://cam.local:5000/focus_absolute/down"
    method: get
```

I then have a Panel dashboard with this card (using [layout-card](https://github.com/thomasloven/lovelace-layout-card) for better grid customisation):
```
type: custom:layout-card
layout_type: custom:grid-layout
layout:
  grid-template-columns: 80% 20%
cards:
  - type: iframe
    url: http://cam.local:8081
  - square: false
    type: grid
    columns: 1
    cards:
      - type: custom:digital-clock
      - show_name: true
        show_icon: true
        type: button
        tap_action:
          action: call-service
          service: rest_command.cam_exposure_down
          target: {}
        icon: mdi:camera-iris
        name: Exposure
      - show_name: true
        show_icon: true
        type: button
        tap_action:
          action: call-service
          service: rest_command.cam_focus_down
          target: {}
        icon: mdi:camera-party-mode
        name: Focus
      - type: gauge
        entity: sensor.phone_battery_level
        severity:
          green: 50
          yellow: 20
          red: 0
        layout_options:
          grid_columns: 1
          grid_rows: 2
        tap_action:
          action: call-service
          service: notify.mobile_app_phone
          target: {}
          data:
            message: Ping!
            data:
              ttl: 0
              priority: high
              media_stream: alarm_stream_max
              tts_text: Hello! Here is your mobile phone!
      - type: gauge
        entity: sensor.tablet_battery
        severity:
          green: 50
          yellow: 20
          red: 0
        layout_options:
          grid_columns: 1
          grid_rows: 2
        tap_action:
          action: call-service
          service: button.press
          target:
            entity_id: button.tablet_load_start_url
columns: 2
layout_options:
  grid_columns: 2
  grid_rows: auto
```
