#import RPi.GPIO as GPIO
import google

import firebase_admin
import self as self
from firebase_admin import credentials
from firebase_admin import firestore

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)

cred = credentials.Certificate('itahome-7e232-firebase-adminsdk-zb413-a77ff39656.json')
firebase_admin.initialize_app(cred)

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
upgaragem =0
ujardin = 0
uvaranda = 0

db = firestore.client()

def controle(pin, status,area):
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
    if (area == "sala"):
        valor = usala
    if (area == "cozinha"):
        valor = ucozinha
    if (area == "quarto"):
        valor  = uquarto
    if (area == "garagem"):
        valor = ugaragem
    if (area == "pgaragem"):
        valor = upgaragem
    if (area == "jardin"):
        valor = ujardin
    if (area == "varanda"):
        valor = uvaranda

    if(valor != status):
        if(status == 1):
            print("Ligado {}".format(area))
            #GPIO.output(pin, GPIO.HIGH)
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

        else:
            print("desligado {}".format(area))
            #GPIO.output(pin, GPIO.HIGH)
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


def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]


casa_ref = db.collection(u'Casas').document(u'1008B1CC1E37')
while 1:
    try:
        doc = casa_ref.get()
        a = doc.to_dict()
        controle(suite,a[u'suite'],"suite")
        controle(sala, a[u'sala'],"sala")
        controle(cozinha, a[u'cozinha'],"cozinha")
        controle(quarto, a[u'quarto'],"quarto")
        controle(garagem, a[u'garagem'],"garagem")
        controle(jardin, a[u'jardin'],"jardin")
        controle(varanda, a[u'varanda'],"varanda")
        controle(pgaragem, a[u'pgaragem'],"pgaragem")
    except google.cloud.exceptions.NotFound:
        casa_ref.set({
            u'suite' :0,
            u'sala' : 0,
            u'cozinha':0,
            u'quarto':0,
            u'garagem':0,
            u'pgaragem':0,
            u'jardin' :0,
            u'varanda':0,
        })

