# TD Watchdog

Component to integrate watchdog heartbeat

## Requirements

- Touchdesigner  >= 2023.12370

## Installation

Copy this directory into the "external" folder on the base directory of your project:

```sh
./external/watchdog
```

Load the tox into your project

In the "Common" page set "Reload custom parameters" to OFF

## Usage

Parameters on page "Input":

| Parameter            | Description                                       |
| :------------------- | :------------------------------------------------ |
| `HeartbeatFrequency` | The frequency the `heartbeat.xml` will be written |
| `HeartbeatPath`      | The path the `Ïheartbeat.xml will` be written to  |
