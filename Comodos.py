#from rpi_rf import RFDevice


envio = 17
suite = 1
sala = 2
cozinha = 3
quarto = 4
garagem = 5
pgaragem = 6
jardin = 7
varanda = 8
usuite = 0
usala = 0
ucozinha = 0
uquarto = 0
ugaragem = 0
upgaragem = 0
ujardin = 0
uvaranda = 0

def controles(status, area):
    global usuite
    global usala
    global ucozinha
    global uquarto
    global ugaragem
    global upgaragem
    global ujardin
    global uvaranda
    global suite
    global sala
    global cozinha
    global quarto
    global garagem
    global pgaragem
    global jardin
    global varanda
    global envio
    if (area == "suite"):
        valor = usuite
        pin = suite
    if (area == "sala"):
        valor = usala
        pin = sala
    if (area == "cozinha"):
        valor = ucozinha
        pin = cozinha
    if (area == "quarto"):
        valor = uquarto
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
    if (valor != status):
        if (status == 1):
            print("Ligado {}".format(area))
            if (area == "suite"):
                usuite = status
            if (area == "sala"):
                usala = status
            if (area == "cozinha"):
                ucozinha = status
            if (area == "quarto"):
                uquarto = status
            if (area == "garagem"):
                ugaragem = status
            if (area == "pgaragem"):
                upgaragem = status
            if (area == "jardin"):
                ujardin = status
            if (area == "varanda"):
                uvaranda = status
        else:
            print("desligado {}".format(area))
            if (area == "suite"):
                usuite = status
            if (area == "sala"):
                usala = status
            if (area == "cozinha"):
                ucozinha = status
            if (area == "quarto"):
                uquarto = status
            if (area == "garagem"):
                ugaragem = status
            if (area == "pgaragem"):
                upgaragem = status
            if (area == "jardin"):
                ujardin = status
            if (area == "varanda"):
                uvaranda = status
#           rfdevice = RFDevice(envio)
#           rfdevice.enable_tx()
#           rfdevice.tx_code(pin, 1,130)
#           rfdevice.cleanup()

