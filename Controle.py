from subprocess import call


def controlarTv(action):
    casa_ref.child("tv").remove()
    print(action)
    if (action == "power"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_POWER"])
    if (action == "input"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_TV"])
    if (action == "volume+"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    if (action == "volume-"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    if (action == "0"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_0"])
    if (action == "1"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_1"])
    if (action == "2"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_2"])
    if (action == "3"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_3"])
    if (action == "4"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_4"])
    if (action == "5"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_5"])
    if (action == "6"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_6"])
    if (action == "7"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_7"])
    if (action == "8"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_8"])
    if (action == "9"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_9"])
    if (action == "chanel+"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_CHANNELUP"])
    if (action == "chanel+"):
        call(["irsend", "SEND_ONCE", "tv", "KEY_CHANNELDOWN"])


def controlarSom(action):
    casa_ref.child("som").child("action").remove()


def controlarAr(action):
    casa_ref.child("ar").child("action").remove()
