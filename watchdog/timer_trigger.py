def onValueChange(channel, sampleIndex, val, prev):
    op('heartbeat_timer').par.start.pulse()
