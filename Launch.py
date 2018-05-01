import pyrebase
from Comodos import controles
from Controle import controlarTv
from Cameras import init

config = {
  "apiKey": "AIzaSyAo5ltguHccSiW_kHNINyktfV3mzZlYZQk",
  "authDomain": "itasmart-b75a1.firebaseapp.com",
  "databaseURL": "https://itasmart-b75a1.firebaseio.com",
  "storageBucket": "itasmart-b75a1.appspot.com",
  "serviceAccount":"itasmart-b75a1-firebase-adminsdk-4ueh4-3896b72e8f.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


def stream_handler(mensagem):
        if(len(mensagem["path"]) > 3):
            caminho = mensagem["path"].split('/')
            if(caminho[3] == 'comodos'):
                controles(mensagem["data"],caminho[4])
            if(caminho[3] == "controle"):
                    acao = mensagem["data"]
                    if(caminho[4] == "tv"):
                        if(acao != None):
                                controlarTv(acao)



def getMAC(interface='eth0'):
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
init()
