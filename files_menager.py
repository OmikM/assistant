import pandas as pd
import enquiries
class files_menager:
  def print(df):
    try:
      print(pd.read_csv(df+'.csv'))
    except FileNotFoundError:
      print("no such file")

  def addcolumn(df):
    rows = []
    a =len(df.index)
    for i in range(a):
      rows =rows+ [input(str(i+1)+" row: ")]
      print(rows)
    a =input("column name: ")
    df[a]= rows
    return df
  
  def addrow(df):
    rows = []
    for i in range(len(df.columns)):
      df = df.append({df.columns[i]: input()}, ignore_index=True)
    
    
    df.append(rows)
    return df
    
    
  def buildMode(*args, **kwargs):

    options = ["create new" , "edit"]
    choice = enquiries.choose("what?",options)
    if choice=="create new":
      df = pd.DataFrame()
      print(df)
      nazwa = input("df name :")
    elif choice=="edit":
      nazwa = input('enter name: ')
      df = pd.read_csv(nazwa+'.csv')
    while True:
      print(df)
      options = ["add column" , "add row", 'Done']
      choice = enquiries.choose("what?",options)
      if choice=='add column':
        df = files_menager.addcolumn(df)
      if choice=='add row':
        df = files_menager.addrow(df)
      elif choice=='Done':
        df.to_csv(nazwa+'.csv')
        break


#lista_a = pd.read_csv('nazwa_pliku.csv')
#lista_a = lista_a[["Nazwa", "Trudność"]]
#print(lista_a)
#new_row ={"Nazwa":input("podaj nazwę: "),"Trudność":int(input("podaj trudność"))}
#lista_a = lista_a.append(new_row, ignore_index=True)



#lista_a = pd.DataFrame(lista_a)
#lista_a.columns = "Nazwa", "Trudność"
# tylko 3 trudność print( "\n\n\n\n" ,lista_a.loc[:2, ["Trudność"]])
#print(lista_a)
#for index, row in lista_a.iterrows():
 # if row["Trudność"] > 3:
 #   print(row["Nazwa"],"-", row["Trudność"])
#lista_a.to_csv('nazwa_pliku.csv')
#print()