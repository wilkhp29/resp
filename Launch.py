import RPi.GPIO as GPIO
from subprocess import call
import pyrebase
import Lirc
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

config = {
  "apiKey": "AIzaSyC01bcx-excaCLw8qp_OUq8cRirHvHnjdw",
  "authDomain": "itahome-7e232.firebaseapp.com",
  "databaseURL": "https://itahome-7e232.firebaseio.com",
  "storageBucket": "itahome-7e232.appspot.com",
  "serviceAccount":"itahome-7e232-firebase-adminsdk-zb413-a77ff39656.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase
suite = 4
sala = 17
cozinha = 18
quarto = 27
garagem = 22
pgaragem = 23
jardin = 24
varanda = 25

usuite = 0
usala = 0
ucozinha = 0
uquarto = 0
ugaragem = 0
upgaragem = 0
ujardin = 0
uvaranda = 0

db = firebase.database()

call(["modprobe","lirc_rpi","gpio_in_pin=24","gpio_out_pin=23"])
call(["service","lirc","start"])


def controlarTv(action):
    casa_ref.child("tv").child("action").remove()
    print(action)
        if(action == "power"):
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

def stream_handler(mensagem):
        if(len(mensagem["path"]) > 3):
            caminho = mensagem["path"].split('/')   / -K7yGTTEp7O549EzTYtI
            if(caminho[3] == 'comodos'):
                controle(mensagem["data"],caminho[4])   {'title': 'Pyrebase', " body ":" etc ... "}
            if(caminho[3] == "controle"):
                    acao = mensagem["data"]
                    if(caminho[4] == "tv"):
                        if(acao != None):
                                controlarTv(acao)


def controle(status,area):
    global usuite
    global usala
    global ucozinha
    global uquarto
    global ugaragem
    global upgaragem
    global ujardin
    global uvaranda
    if(area == "suite"):
        valor = usuite
        pin = suite
    if (area == "sala"):
        valor = usala
        pin = sala
    if (area == "cozinha"):
        valor = ucozinha
        pin = cozinha
    if (area == "quarto"):
        valor  = uquarto
        pin = quarto
    if (area == "garagem"):
        valor = ugaragem
        pin = garagem
    if (area == "pgaragem"):
        valor = upgaragem
        pin = pgaragem
    if (area == "jardin"):
        valor = ujardin
        pin = jardin
    if (area == "varanda"):
        valor = uvaranda
        pin = varanda
    if(valor != status):
        if(status == 1):
            print("Ligado {}".format(area))
            if (area == "suite"):
                 usuite = status
            if (area == "sala"):
                 usala = status
            if (area == "cozinha"):
                ucozinha =status
            if (area == "uquarto"):
                 status =status
            if (area == "garagem"):
                ugaragem = status
            if (area == "pgaragem"):
                upgaragem =status
            if (area == "jardin"):
                ujardin = status
            if (area == "varanda"):
                uvaranda = status
            GPIO.output(pin, GPIO.HIGH)
        else:
            print("desligado {}".format(area))
            if (area == "suite"):
                usuite = status
            if (area == "sala"):
                usala = status
            if (area == "cozinha"):
                ucozinha = status
            if (area == "uquarto"):
                status = status
            if (area == "garagem"):
                ugaragem = status
            if (area == "pgaragem"):
                upgaragem = status
            if (area == "jardin"):
                ujardin = status
            if (area == "varanda"):
                uvaranda = status
            GPIO.output(pin, GPIO.HIGH)

def getMAC(interface='eth0'):
   Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17].replace(":","")
id = getMAC("eth0")

casa_ref = db.child("Casas").child(id)
casa_ref.child("comodos").set({
    u'suite': 0,
    u'sala': 0,
    u'cozinha': 0,
    u'quarto': 0,
    u'garagem': 0,
    u'pgaragem': 0,
    u'jardin': 0,
    u'varanda': 0,
})
my_stream = casa_ref.stream(stream_handler)

