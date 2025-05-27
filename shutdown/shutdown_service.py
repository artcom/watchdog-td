def onOnToOff(channel, sampleIndex, val, prev):
    op('udpout').sendBytes('halt')

