#archivo LibDNI.py
def calculoLetra(numerodni):
  letras=("TRWAGMYFPDXBNJZSQVHLCKE")
  dni=int(input("Introduzca los números de su DNI aquí porfavor: "))
  numero = numerodni%23
  numeroL = numero(dni)
  letra = letras[numeroL]
  return letra
