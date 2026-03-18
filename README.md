# TD Watchdog

Component to integrate watchdog heartbeat

## Requirements

- Touchdesigner  >= 2023.12370

## Installation

Copy this directory into the "external" folder on the base directory of your project:

```sh
./external/watchdog
```

Load the tox into your project:

1. drag into your project
2. Common -> Enable External .tox = ON
3. Common -> External .tox Path = set to tox file
4. Common -> Reload custom parameters = OFF

## Usage

Parameters on page "Input":

| Parameter            | Description                                       |
| :------------------- | :------------------------------------------------ |
| `HeartbeatFrequency` | The frequency the `heartbeat.xml` will be written |
| `HeartbeatPath`      | The path the `Ïheartbeat.xml will` be written to  |
