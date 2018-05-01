from datetime import datetime
import requests
from pyrebase import pyrebase

config = {
  "apiKey": "AIzaSyAo5ltguHccSiW_kHNINyktfV3mzZlYZQk",
  "authDomain": "itasmart-b75a1.firebaseapp.com",
  "databaseURL": "https://itasmart-b75a1.firebaseio.com",
  "storageBucket": "itasmart-b75a1.appspot.com",
  "serviceAccount":"itasmart-b75a1-firebase-adminsdk-4ueh4-3896b72e8f.json"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()
ultimoIp = ""

now = datetime.now()
def getMyIp():
    global ultimoIp
    url = 'http://myexternalip.com/raw'
    r = requests.get(url)
    ip = r.text
    if(ip != ultimoIp):
        db.child("Casas").child(id).child("myip").set(ip)
        ultimoIp = ip

def getMAC(interface='eth0'):
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17].replace(":","")
id = getMAC("eth0")
udia = 0

def uploadStorage():
    global udia
    if(now.day < 10):
        dia = "0{}".format(now.day)
    else:
        dia = now.day
    if (now.month < 10):
        mes = "0{}".format(now.month)
    else:
        mes = now.month
    storage.child(id).child("cameras").child("camera1").child("{}-{}-{}.avi".format(dia,mes,now.year)).put("{}-{}-{}.avi".format(now.day,now.month,now.year))
    url = storage.child(id).child("cameras").child("camera1").child("{}-{}-{}.avi".format(dia, mes, now.year)).get_url(None)
    if(udia != now.day):
        db.child("Casas").child(id).child("cameras").child("camera1").child("url").set(url)
        udia = now.day