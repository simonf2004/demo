def connectToWifiAndUpdate():
    import time, machine, network, gc
    time.sleep(1)
    print('Memory free', gc.mem_free())

    from app.ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('AP_FZ', '7304162657')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    otaUpdater = OTAUpdater('https://github.com/simonf2004/demo')
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        machine.reset()
    else:
        del(otaUpdater)
        gc.collect()

def startApp():
    import app.start


connectToWifiAndUpdate()
startApp()

