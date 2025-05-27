def onValueChange(channel, sampleIndex, val, prev):
    op('udpout').sendBytes('halt')
