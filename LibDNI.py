#archivo LibDNI.py
def calculoLetra(dni):
  letras = "TRWAGMYFPDXBNJZSQVHLCKE"
  letra = letras[dni%23]
  return letra
