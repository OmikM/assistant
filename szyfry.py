class szyfr():
  
  def szyfr(cos):
    import random
    tekst = input("Podaj hasło do zaszyfrownaia: ")
    for i in range(len(tekst)):
      a = random.randint(1,9)
      kod = ord(tekst[i])+a
      if len(str(kod))==2:
         cos =cos+str(a) + "0"+str(kod)    
      else:
        cos = cos +str(a)+ str(kod)
    print(cos)

  def odszyfr():
    cos = input("odszyfruj: ")
    b = int(cos[0])
    for i in range(len(cos)//4):
      b = int(cos[i*4])
      cos= str(int(cos) - b)
      litera = cos[i*3+1]+cos[i*3+2]+cos[i*3+3]
      litera = int(litera)
      print(chr(litera))
# chr() numer -> znak
# ord() znak -> numer