import time, random #, pygame
from libery import funkcje as f
from replit import db
from szyfry import szyfr

import enquiries
from files_menager import files_menager as fm

# posible ficher window
#ok = Tk()
#ok.title = ("Asystent")
#ok.geometry = ("200x300")
#ok.configure(background='#111d35')
#l_input = Label(bg="black",text="TAK", width=10, height=3)
#l_input.pack()
#l_output = Label(bg="#111d35",text="TAK", width=10, height=3)
#l_output.pack()

#hasła
while True:
  options = ["sing in" , "log in"]
  odp = enquiries.choose('Choose one of these options: ', options)
  if odp=="sing in":
    db["password"] += " [" + input("name: ")+"] "
  if odp=="log in":
    odp = input("password: ")
    tak = db["password"].count(odp)
    if tak>0:
      break
      
while True:
  odp = input("co chcesz zrobić: ")
  if odp == "pesel":
    f.pesel()
  elif odp == 'help':
    print("sth")
  elif odp == 'close' or odp == 'quit':
    break
  elif odp=="szyfr":
    szyfr.szyfr("")
  elif odp=="odszyfr":
    szyfr.odszyfr()
  elif odp == "print_df":
    fm.print(input("what dataframe?"))
  elif odp == "c":
    fm.buildMode()
    


#ok.mainloop()