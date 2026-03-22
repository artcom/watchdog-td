from datetime import datetime, timezone


def onCycle(timerOp, segment, cycle):
    path = str(parent().par.Heartbeatpath)

    secs = datetime.now(timezone.utc).timestamp()
    xml = f'<Heartbeat secondsSince1970="{secs}"></Heartbeat>'

    with open(path, "w", encoding="utf-8") as f:
        f.write(xml)
