camcontrol
==========

A project to expose v4l2-ctl configuration to home assistant on my lan. Runs on the camera-operating system (pi 4 in my case)

Home Assistant config
---------------------

```
rest_command:
  cam_exposure_up:
    url: "http://192.168.0.249:5000/exposure_time_absolute/up"
    method: get
  cam_exposure_down:
    url: "http://192.168.0.249:5000/exposure_time_absolute/down"
    method: get
  cam_focus_up:
    url: "http://192.168.0.249:5000/focus_absolute/up"
    method: get
  cam_focus_down:
    url: "http://192.168.0.249:5000/focus_absolute/down"
    method: get
```

I then have a Panel dashboard with this card (using [layout-card](https://github.com/thomasloven/lovelace-layout-card) for better grid customisation):
```
type: custom:layout-card
layout_type: custom:grid-layout
layout:
  grid-template-columns: 90% 10%
cards:
  - camera_view: live
    type: picture-glance
    entities: []
    camera_image: camera.front_camera
    title: Front
  - square: false
    type: grid
    columns: 1
    cards:
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
columns: 2
layout_options:
  grid_columns: 2
  grid_rows: auto
```
