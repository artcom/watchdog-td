def onInitialize(timerOp, callCount):
    return 0


def onDone(timerOp, segment, interrupt):
    # called when shutdown finished
    op.ShutdownService.par.Shutdown.pulse()
    return
