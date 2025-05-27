# PLM Kinetic Control

Sketch to control the kinetic over MQTT.

## Requirements

- Touchdesigner

## Content

| Directory      | Description                                                                      |
| :------------- | :------------------------------------------------------------------------------- |
| playground.toe | Everything wired up                                                              |
| shutdown       | Receives shutdown trigger and schedules timer to send "halt" via UDP to watchdog |
| watchdog       | Writes a heartbeat.xml to disk.                                                  |
