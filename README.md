# TD Watchdog

Example to integrate watchdog and controlled shutdown into TouchDesigner sketches.

## Requirements

- Touchdesigner

## Content

| Components     | Description                                                                      |
| :------------- | :------------------------------------------------------------------------------- |
| playground.toe | Everything wired up                                                              |
| shutdown       | Receives shutdown trigger and schedules timer to send "halt" via UDP to watchdog |
| watchdog       | Writes a heartbeat.xml to disk.                                                  |
