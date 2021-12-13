class szyfr():
  
  def szyfr(cos):
    import random
    tekst = input("Podaj hasło do zaszyfrownaia: ")
    for i in range(len(tekst)):
      print('Done',i,"/",len(tekst), end="\r")
      a = random.randint(1,9)
      kod = ord(tekst[i])+a
      if len(str(kod))==2:
         cos =cos+str(a) + "0"+str(kod)    
      else:
        cos = cos +str(a)+ str(kod)
    print(cos)

  def odszyfr():
    wynik = ""
    cos = input("odszyfruj: ")
    
    for i in range(len(cos)//4):
      print(cos)
      print(-(i*3))
      litera = cos[(i*4+3)*-1]+cos[(i*4+2)*-1]+cos[(i*4+1)*-1]
      
      litera = int(litera) - int(cos[(i*4+4)*-1])
      litera = chr(litera)
      print(litera)
      wynik = wynik+litera
    print(wynik )
# chr() numer -> znak
# ord() znak -> numer