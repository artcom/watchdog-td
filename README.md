# TD Watchdog

TD Component to integrate watchdog heartbeat

## Requirements

- Touchdesigner  >= 2025

## Installation

Add this dependency to your `requirements.txt`:

```sh
watchdog-td @ git+https://github.com/artcom/watchdog-td.git@0.1.0#egg=watchdog-td
```

Load the tox into your project:

1. create a baseCOMP
2. Common -> External .tox Path = `mod.watchdog_td.ToxFile`
3. Common -> Enable External .tox = ON
4. Common -> Reload custom parameters = OFF

## Usage

Parameters on page "Input":

| Parameter            | Description                                       |
| :------------------- | :------------------------------------------------ |
| `HeartbeatFrequency` | The frequency the `heartbeat.xml` will be written |
| `HeartbeatPath`      | The path the `Ïheartbeat.xml will` be written to  |
