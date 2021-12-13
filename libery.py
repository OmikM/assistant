class funkcje:
  def pesel():
    a = int(input("podaj pesel: "))
    if len(str(a))== 11:
      print("pog")
      rok =str(a)[-2]+str(a)[-1]
      print(rok)
    else:
     print("Nie fajnie")
