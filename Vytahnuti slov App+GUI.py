#Program funkcni v.0.2.alfa
#HOTOVO - Vytvorit hlavni nabidku
#Nabidka soubor
#   Otevrit soubor HOTOVO
#                   HOTOVO - Zajistit prekreslovani okna pri zmene menu
#                   HOTOVO - vsechny widgety zabalit do Framu
#                   HOTOVO - Zvolit nazev projektu
#                   HOTOVO - Vyvorit slozku s projektem
#                   HOTOVO - Zkontrolavat jestli projekt uz neexistuje
#                   HOTOVO - Spocitat neroztridena slova
#                   HOTOVO - Vypsat neroztridena slova do seznamu
#                   HOTOVO - procentualni graf nacitani projektu nebo neco podobneho
#                   Tlacitko prevod do slovniku znamych slov
#                           HOTOVO - ulozit do souboru  slovniku znamych slov projektu
#                           +HotKey
#                   Tlacitko prevod do slovniku neznamych slov
#                           HOTOVO - ulozit do souboru  slovniku neznamych slov projektu
#                           +HotKey
#   HOTOVO - Projekty Komletni
#   HOTOVO - Projekty Rozpracovane
#                       HOTOVO - vybrat slova nedulezita nebo neprelozitelna 
#                       HOTOVO - pridat znama a neznama slova z projektu do hlavnich slovniku
#Zjistene chyby a nedostatky, 
#       Hotovo - Pokud je seznam slov vytriden hned na prvni pokus, nedojde k prepnuti do rezim dokonceni
#       HOTOVO - Pridat tlacitko pro preved vsech slov do urciteho seznamu




from tkinter import filedialog#nacte knihovnu File Dialog
from tkinter import*#nacte vse z knihovny Tkinter
import os #importuje knihovnu os
from shutil import copy2#nacte z knihovny shutil funkci copy2(pro kopirovani souboru)

root=Tk()#  nacte tkinter
root.minsize(700, 400) # nastavi minimalni velikost okna sirka/vyska

jmeno=StringVar() #tkinter promena pro novy projekt
jmeno.set('') #nastaveni promene pro nazev nove projektu
root.title("Vyhledani slov z titulku")#Zmeni nazev okna
root.option_add('*Font', 'serif 8') # protože defaultní písmo pod Windows je hrozné

def hello(): #pomocne pri tvorbe programu
    print( "Ahoj!")
def callback():
    print("Kliknul jsi!") #pomocne pri tvorbe programu
    
  
def otevriazjistinazevsouboru():#otevre okno pro hledani souboru a vrati jeho jmeno a cestu k nemu ve String
    root.jmenosouboru= filedialog.askopenfilename(initialdir = "/",title = "Vyber soubor",filetypes = (("all files","*.*"),("subtitles files","*.sub"),("text files","*.txt"),("jpeg files","*.jpg")))
    return(str(root.jmenosouboru))
                   

def Soubor_Otevrit():##Funkce menu Soubor/vytvorit novy projekt
    vycistihlavniramec()#vymaze vse z hlavniho ramce
    ####zjisti jmeno projektu
    def zmena():#po zmacknuti tlacitka kontroluje zda je zapsana nova hodnota do vstupu
        if nazev.get()!='': #kdyz je hodnota ve widgetu Entry zmenena odstrani Button a Entry
            existuje=False
            for projekt in os.listdir('Projekty'): #zkontroluje zda je Projekt jiz vytvoren
                if projekt==nazev.get():
                    popisek2=Label(hlavniramec,text='Projekt:'+nazev.get()+' . Jiz existuje, vyber jiny nazev')
                    popisek2.grid(row=2,column=0)
                    nazev.delete(0,END)
                    print('Tento projekt existuje')
                    existuje=True
            if existuje==False:
                jmeno.set(nazev.get())#ulozi hodnotu z Entry do tkinter promenne
                vycistihlavniramec()
                
                cestaksouboru=otevriazjistinazevsouboru()
                
                while cestaksouboru=='':
                    cestaksouboru=otevriazjistinazevsouboru()
                print(cestaksouboru,' ',jmeno.get())
                vytvor_seznam2(cestaksouboru,jmeno.get())#vytvori seznam
    popisek=Label(hlavniramec,text='Zadej nazev projektu')#vytvori Label
    popisek.grid(row=0,column=0)#ukaze Label
    nazev=Entry(hlavniramec)#vytvori Entry 
    nazev.grid(row=1,column=0)#ukaze Entry
    tlacitko=Button(hlavniramec,text='Vytvor projekt',command=zmena)#vytvori Button- 
    tlacitko.grid(row=1,column=1)#ukaze Button

    
def Kompletne_hotove(): #funkce pro menu Projekty/Kompletne hotove
    def ukaz_projekt():#nacte vybrany projekt
        dokoncitprojekt(seznamhotovych.get(seznamhotovych.curselection()))
    vycistihlavniramec()
    stitekkompletne=Label(hlavniramec,text="Kompletne hotove")#vytvori Label
    stitekkompletne.grid(row=0,column=0)
    seznamhotovych=Listbox(hlavniramec)#vytvori Listbox
    seznamhotovych.grid(row=1, column=0)
    for projekty in os.listdir('Projekty'):#zjisti ktere projekty jsou Kompletne hotove
        init=open('Projekty/'+projekty+'/init','r')
        if init.readline()=='kompletni':
            seznamhotovych.insert(END,projekty)#vypise do seznamu
        init.close()
    if seznamhotovych.get(0)!='':#pokud neni seznam prazdny tak vytvori tlacitko
        tlzobraz=Button(hlavniramec, text='Otevri projekt',command=ukaz_projekt)
        tlzobraz.grid(row=1, column=1)
    
        
def vytvor_seznam2(cestaksouboru,projekt):# vytvori seznam neztridenich slov
    #prijima parametry(ceska k souboru, nazev projektu 
    pomoc=False
    for soubor in os.listdir('Projekty/'):
        if soubor==projekt:
            pomoc=True
    if pomoc==False:    
        os.mkdir('Projekty/'+projekt)#vytvori slozku Projektu
        copy2(cestaksouboru, 'Projekty/'+projekt+'/'+projekt+'-orig.txt') # complete target filename given
        projektnez=open('Projekty/'+projekt+'/'+'Neznama slova.txt','w')
        projektnez.close()
        projektzna=open('Projekty/'+projekt+'/Znama slova.txt','w')
        projektzna.close()
        projektnep=open('Projekty/'+projekt+'/Neprelozitelna slova.txt','w')
        projektnep.close()
        kompletnost=open('Projekty/'+projekt+'/init','w')
        kompletnost.write('nekompletni')
        kompletnost.close()
    print('Chvilku strpeni, prohledava se soubor...')
    nazevprojektu=Label(hlavniramec, text='Projekt: '+projekt,font=('Arial',15))
    nazevprojektu.grid(columnspan=3,row=0, column=0)
    ####Vytvori seznam neroztridenych slov
    scrollbar = Scrollbar(hlavniramec, orient=VERTICAL)
    seznam = Listbox(hlavniramec,selectmode=MULTIPLE,font=('Arial',15),yscrollcommand=scrollbar.set)
    scrollbar.config(command=seznam.yview)
    scrollbar.grid(sticky=W+E+N+S,rowspan=2,row=2, column=1)
    seznam.config(height=20)
    seznam.selection_set(first=1,last=3)
    seznam.grid(sticky=W,rowspan=2,row=2, column=0)#Ulozi do mrizky na pozici 1,0(radek,sloupec)
    #######################
    nactenysoubor=open(cestaksouboru,'r')#otevre soubor pro cteni
    delka=len(nactenysoubor.read())#zjisti pocet znaku v souboru
    nactenysoubor=open(cestaksouboru,'r')#otevre soubor pro cteni
    index=1 #pomocne pro cyklus while
    poradipismena=1
    slovo=''
    kontrolaseznamu=False
    pocetslov=0
    pomoc4=True
    a=0#pomoc pro graf
    procento=delka/25#4%grafu
    while index<=delka: #nacte postupne cela slova ze souboru a ulozi do slovo
        #if index//procento
        eng=nactenysoubor.read(1)#nacte jeden znak
        hodnota=ord(eng)#prevede do ASCII hodnoty
        if (hodnota==39) or ((hodnota>=65)and(hodnota<=90)) or ((hodnota>=97)and(hodnota<=122)): #pokud je pismeno male nebo velke ne znak- ' ulozi ho do slova
            slovo=slovo+chr(hodnota) #chr() prevede ASCII hodnotu na znak
            poradipismena=poradipismena+1
        else:                     
            if poradipismena>1: #pokud je poradi pismena vetsi nez jedna tak mame cele slovo
                slovo=slovo.lower() #prevede vsechna pismena na mala
                #print(slovo,' ',projekt)
                if zkontrolujslovniky(slovo,projekt)==1:
                    for slovovseznamu in seznam.get(0,END):  #prohleda seznam a zjisti jestli obsahuje nove slovo      
                        if slovo==slovovseznamu:
                            kontrolaseznamu=True
                            break
                        else:
                            kontrolaseznamu=False
                    if kontrolaseznamu==False:
                        pocetslov=pocetslov+1
                        seznam.insert(END, slovo)#zapise slovo do seznamu
                slovo=''
            poradipismena=1
        index=index+1
        if index%procento<1:#vypise kolik je nacteno a porovnano znaku ze souboru
            a=a+4
            print('Nacteno: ',a,'% souboru')
    v=StringVar()
    v.set('Pocet neroztridenych slov je: '+str(seznam.size()))
    stitek=Label(hlavniramec,text='Pocet neroztridenych slov je: ', textvariable=v)
    stitek.grid(sticky=W,row=1, column=0)#Ulozi do mrizky na pozici 0,0
    def preveddoznam():#prevede oznacene do slovniku
        projektzna=open('Projekty/'+projekt+'/Znama slova.txt','a')
        for poradi in seznam.curselection():
            projektzna.write(seznam.get(poradi)+'\n')
        projektzna.close()    
        vybrane=seznam.curselection()
        delkavybrane=len(vybrane)
        while delkavybrane!=0:
            delkavybrane=delkavybrane-1 
            seznam.delete(vybrane[delkavybrane])
        v.set('Pocet neroztridenych slov je: '+str(seznam.size()))
        if seznam.size()==0:
            dokoncitprojekt(projekt)
    def preveddonez():
        projektnez=open('Projekty/'+projekt+'/Neznama slova.txt','a')
        for poradi in seznam.curselection():
            projektnez.write(seznam.get(poradi)+'\n')
        projektnez.close()    
        vybrane=seznam.curselection()
        delkavybrane=len(vybrane)
        while delkavybrane!=0:
            delkavybrane=delkavybrane-1 
            seznam.delete(vybrane[delkavybrane])
        v.set('Pocet neroztridenych slov je: '+str(seznam.size()))
        if seznam.size()==0:
            dokoncitprojekt(projekt)
    def prevedvsedoznam():#prevede oznacene do slovniku
        projektzna=open('Projekty/'+projekt+'/Znama slova.txt','a')
        for slovo in seznam.get(0,END):
            projektzna.write(slovo+'\n')
        projektzna.close()    
        seznam.delete(0,END)
        v.set('Pocet neroztridenych slov je: '+str(seznam.size()))
        if seznam.size()==0:
            dokoncitprojekt(projekt)
    def prevedvsedoneznam():#prevede oznacene do slovniku
        projektzna=open('Projekty/'+projekt+'/Neznama slova.txt','a')
        for slovo in seznam.get(0,END):
            projektzna.write(slovo+'\n')
        projektzna.close()    
        seznam.delete(0,END)
        v.set('Pocet neroztridenych slov je: '+str(seznam.size()))
        if seznam.size()==0:
            dokoncitprojekt(projekt) 
    tlacitkoznam=Button(hlavniramec,bd=4, text="Prevest\ndo \nslovniku\nznamych\nslov", command=preveddoznam)
    tlacitkoznam.grid(sticky=W+E+N+S,row=2, column=2)#Ulozi do mrizky na pozici 1,2(radek,sloupec)
    tlacitkovseznam=Button(hlavniramec, text="Prevest vse\ndo \nslovniku\nznamych\nslov", command=prevedvsedoznam)
    tlacitkovseznam.grid(sticky=W+E,row=2, column=3)#Ulozi do mrizky na pozici 1,2(radek,sloupec)
    tlacitkoneznam=Button(hlavniramec, text="Prevest\ndo \nslovniku\nneznamych\nslov", command=preveddonez)
    tlacitkoneznam.grid(sticky=W+E+N+S,row=3, column=2)#Ulozi do mrizky na pozici 1,2(radek,sloupec)
    tlacitkovseneznam=Button(hlavniramec, text="Prevest vse\ndo \nslovniku\nneznamych\nslov", command=preveddonez)
    tlacitkovseneznam.grid(sticky=W+E,row=3, column=3)#Ulozi do mrizky na pozici 1,2(radek,sloupec)

    nactenysoubor.close()#zavre soubor
    if seznam.size()==0:#pokud je seznam prazdny tak jej prepne pro dokonceni
        dokoncitprojekt(projekt)

def dokoncitprojekt(projekt):#umoznuje dokoncit projekt(doupravit slovniky (Ne)Znamych a neprelozitelnych slov)
    vycistihlavniramec()
    nazev=Label(hlavniramec,text='Nazev projektu: '+projekt)
    nazev.grid(row=0,column=0)
    robrazitnez=Button(hlavniramec,text='Zobrazit neznama slova',command=lambda:zobrazitslova(projekt,'nez'))
    robrazitnez.grid(row=1,column=0)
    robrazitzna=Button(hlavniramec,text='Zobrazit znama slova',command=lambda:zobrazitslova(projekt,'zna'))
    robrazitzna.grid(row=1,column=2)
    robrazitnep=Button(hlavniramec,text='Zobrazit slova neprelozitelna a nedulezita',command=lambda:zobrazitslova(projekt,'nep'))
    robrazitnep.grid(row=1,column=3)
    robrazitdok=Button(hlavniramec,text='Dokonci projekt',command=lambda:dokoncit_projekt())
    robrazitdok.grid(row=1,column=4)
    buttonframe=Frame(hlavniramec,bg='red')
    buttonframe.grid(row=2,column=2)
    def dokoncit_projekt():#Ulozi slova z projektu do hlavnich slovniku
        for slovnik  in ('Neznama slova','Znama slova','Neprelozitelna slova'):
            soubor=open('Projekty/'+projekt+'/'+slovnik+'.txt','r')
            pr=soubor.readlines()
            soubor.close()
            soubor=open(slovnik+'/'+slovnik+'.txt','r')
            hlavni=soubor.readlines()
            soubor.close()
            soubor=open(slovnik+'/'+slovnik+'.txt','a')
            pomoc5=False
            for slovo in pr:
                pomoc5=False
                for radek in hlavni:
                    if radek==slovo:
                        pomoc5=True
                if pomoc5==False:
                    soubor.write(slovo)
            soubor.close()
        print('Zapis do hlavnich slovniku skoncil')
        soubor=open('Projekty/'+projekt+'/init','w')
        soubor.write('kompletni')
        soubor.close()
        
    def zobrazitslova(projekt,typ):#prijima nazev projektu a typ slovniku, vypise slova do Listboxu, 
        def preved(kam):#prijima parametr kam, prevede slova do slovniku podle parametru
            for slovnik in ('Neznama slova.txt','Znama slova.txt','Neprelozitelna slova.txt'):#Vyhleda slova z Listboxu ve slovnikach a vymaze je
                for poradi in seznam.curselection():#postupne projede vsechna oznacena slova v Listboxu
                    soubor=open('Projekty/'+projekt+'/'+slovnik,'r')#otevre soubor pro cteni
                    radky=soubor.readlines()#Ulozi kazdy radek souboru do promene
                    soubor.close()
                    soubor=open('Projekty/'+projekt+'/'+slovnik,'w')#otevre soubor pro zapis
                    for radek in radky:#zkontroluje kazdy radek
                        if radek!=(seznam.get(poradi)):#kdyz se radek neshoduje ze slovem v Listboxu
                            soubor.write(radek)#zapise radek do seznamu
                    soubor.close()
            if kam=='zna':#ulozi slova z Lisboxu do slovniku
                soubor=open('Projekty/'+projekt+'/Znama slova.txt','a')
                for poradi in seznam.curselection():
                    soubor.write(seznam.get(poradi))
            if kam=='nez':#ulozi slova z Lisboxu do slovniku
                soubor=open('Projekty/'+projekt+'/Neznama slova.txt','a')
                for poradi in seznam.curselection():
                    soubor.write(seznam.get(poradi))
            if kam=='nep':#ulozi slova z Lisboxu do slovniku
                soubor=open('Projekty/'+projekt+'/Neprelozitelna slova.txt','a')
                for poradi in seznam.curselection():
                    soubor.write(seznam.get(poradi))
            soubor.close()#zavre soubor
            vybrane=seznam.curselection()
            delkavybrane=len(vybrane)#zjisti pocet vyranych polozek v Listboxu
            while delkavybrane!=0:#vymaze slova z Listboxu musi mazat odzadu
                delkavybrane=delkavybrane-1 
                seznam.delete(vybrane[delkavybrane])
        scrollbar = Scrollbar(hlavniramec, orient=VERTICAL)#vytvori posuvnik v Listboxu
        seznam = Listbox(hlavniramec,selectmode=MULTIPLE,font=('Arial',15),yscrollcommand=scrollbar.set)#vytvori Listbox
        scrollbar.config(command=seznam.yview)#priradi Listbox a posuvnik
        scrollbar.grid(sticky=W+E+N+S,rowspan=2,row=2, column=1)#zobrazi posuvnik
        seznam.config(height=20)#nastavi vysku Listboxu
        seznam.selection_set(first=1,last=3)
        seznam.grid(sticky=W,rowspan=2,row=2, column=0)#Ulozi do mrizky na pozici 1,0(radek,sloupec)
        if typ=='nez' :#vypise neznama slova do seznamu
            for widget in buttonframe.winfo_children(): #.winfo_children()-zjisti jmena potomku ve widgetu
                widget.destroy()#vymaze widget
            nez=open('Projekty/'+projekt+'/Neznama slova.txt','r')#otevre soubor
            slovo=nez.readline()#nacte prvni radek
            while slovo!='':#pokud dojede na konec souboru skonci
                seznam.insert(END,slovo)#Vlozi slovo do Listboxu
                slovo=nez.readline()#nacte dalsi radek
            tlpreveddozna=Button(buttonframe,text='Preved do znamych slov',command=lambda:preved('zna'))
            tlpreveddozna.grid(row=0,column=0)
            tlpreveddoned=Button(buttonframe,text='Preved do neprelozitelnych slov',command=lambda:preved('nep'))
            tlpreveddoned.grid(row=1,column=0)

        if typ=='zna' :#vypise znama slova do seznamu
            for widget in buttonframe.winfo_children(): #.winfo_children()-zjisti jmena potomku ve widgetu
                widget.destroy()#.destroy() - vymaze widget
            nez=open('Projekty/'+projekt+'/Znama slova.txt','r')
            slovo=nez.readline()
            while slovo!='':
                seznam.insert(END,slovo)
                slovo=nez.readline()
            tlpreveddonez=Button(buttonframe,text='Preved do neznamych slov',command=lambda:preved('nez'))
            tlpreveddonez.grid(row=0,column=0)
            tlpreveddoned=Button(buttonframe,text='Preved do neprelozitelnych slov',command=lambda:preved('nep'))
            tlpreveddoned.grid(row=1,column=0)
            
        if typ=='nep' :#vypise neprelozitelna slova do seznamu
            for widget in buttonframe.winfo_children(): #.winfo_children()-zjisti jmena potomku ve widgetu
                widget.destroy()#.destroy() - vymaze widget
            nez=open('Projekty/'+projekt+'/Neprelozitelna slova.txt','r')
            slovo=nez.readline()
            while slovo!='':
                seznam.insert(END,slovo)
                slovo=nez.readline()
            tlpreveddonez=Button(buttonframe,text='Preved do neznamych slov',command=lambda:preved('nez'))
            tlpreveddonez.grid(row=0,column=0)
            tlpreveddozna=Button(buttonframe,text='Preved do znamych slov',command=lambda:preved('zna'))
            tlpreveddozna.grid(row=1,column=0)

def zkontrolujslovniky(slovo,projekt): #vraci hodnotu 0 nebo 1,zjisti jestli slovov v souboru. Hlida slovnik znamych,neznamych a neprelozitelnych slov a slovnik znamych,neznamych a neprelozitelnych slov v nedokoncenem projektu
      #vyhledavani slov ve slovniku znamych slov
      pomoc3=False
    #Prohleda slovnik znamych slov v nedokoncenem projektu
      znameslovo=open('Projekty/'+projekt+'/Znama slova.txt','r')   #otevre soubor  
      znameslovosl=znameslovo.readline() #nacte slovo z prvni radky
      delkazs=len(znameslovosl) #zjisteni delky slova 
      while znameslovosl!='': #vyhledava slovo ve slovniku znamych slov dokud nedojede do konce
           if znameslovosl[:delkazs-1]==(slovo):# znameslovosl[:delkans-1] toto odstrani znak noveho radku po funkci readline
                 pomoc3=True
           znameslovosl=znameslovo.readline() #nacte dalsi radek
           delkazs=len(znameslovosl) #zjisti delku slova na radku
      znameslovo.close() #zavre soubor Znama slova.txt
      if pomoc3==True:
          return 0 #vraci nulu

    #Prohleda slovnik neznamych slov v nedokoncenem projektu
      znameslovo=open('Projekty/'+projekt+'/Neznama slova.txt','r')     
      znameslovosl=znameslovo.readline() #nacte slovo z prvni radky
      delkazs=len(znameslovosl) #zjisteni delky slova 
      while znameslovosl!='': #vyhledava slovo ve slovniku znamych slov dokud nedojede do konce
           if znameslovosl[:delkazs-1]==(slovo):# znameslovosl[:delkans-1] toto odstrani znak noveho radku po funkci readline
                 pomoc3=True
           znameslovosl=znameslovo.readline() #nacte dalsi radek
           delkazs=len(znameslovosl) #zjisti delku slova na radku
      znameslovo.close() #zavre soubor Znama slova.txt
      if pomoc3==True:
          return 0
    #Prohleda slovnik neprelozitelnych slov v nedokoncenem projektu
      znameslovo=open('Projekty/'+projekt+'/Neprelozitelna slova.txt','r')     
      znameslovosl=znameslovo.readline() #nacte slovo z prvni radky
      delkazs=len(znameslovosl) #zjisteni delky slova 
      while znameslovosl!='': #vyhledava slovo ve slovniku znamych slov dokud nedojede do konce
           if znameslovosl[:delkazs-1]==(slovo):# znameslovosl[:delkans-1] toto odstrani znak noveho radku po funkci readline
                 pomoc3=True
           znameslovosl=znameslovo.readline() #nacte dalsi radek
           delkazs=len(znameslovosl) #zjisti delku slova na radku
      znameslovo.close() #zavre soubor Znama slova.txt
      if pomoc3==True:
          return 0

    #Prohleda slovnik znamych slov
      znameslovo=open('Znama slova/Znama slova.txt','r')     
      znameslovosl=znameslovo.readline() #nacte slovo z prvni radky
      delkazs=len(znameslovosl) #zjisteni delky slova 
      while znameslovosl!='': #vyhledava slovo ve slovniku znamych slov dokud nedojede do konce
           if znameslovosl[:delkazs-1]==(slovo):# znameslovosl[:delkans-1] toto odstrani znak noveho radku po funkci readline
                 pomoc3=True
                 projektzna=open('Projekty/'+projekt+'/Znama slova.txt','a')
                 projektzna.write(slovo+'\n')
                 projektzna.close()
           znameslovosl=znameslovo.readline() #nacte dalsi radek
           delkazs=len(znameslovosl) #zjisti delku slova na radku
      znameslovo.close() #zavre soubor Znama slova.txt
    #Prohleda slovnik neznamych slov
      neznameslovo=open('Neznama slova/neznama slova.txt','r')#otevreni pro cteni
      neznameslovosl=neznameslovo.readline() #nacteni prvni radky
      delkans=len(neznameslovosl) #zjisteni delky slova 
      while neznameslovosl!='':#opakuje dokud nedojde ke konci souboru
            if neznameslovosl[:delkans-1]==(slovo):# neznameslovosl[:delkans-1] toto odstrani znak noveho radku po funkci readline
                  pomoc3=True #Pokud nezname slovo najde ve slovniku zmeni na true
                  projektnez=open('Projekty/'+projekt+'/Neznama slova.txt','a')
                  projektnez.write(slovo+'\n')
                  projektnez.close()
                  #print('2 ',pomoc3)
            neznameslovosl=neznameslovo.readline()#nacte dalsi radku
            delkans=len(neznameslovosl)#zjisti delku slova
      neznameslovo.close()#uzavreni souboru
    #Prohleda slovnik neprelozitelnych slov
      neznameslovo=open('Neprelozitelna slova/Neprelozitelna slova.txt','r')#otevreni pro cteni
      neznameslovosl=neznameslovo.readline() #nacteni prvni radky
      delkans=len(neznameslovosl) #zjisteni delky slova 
      while neznameslovosl!='':#opakuje dokud nedojde ke konci souboru
            if neznameslovosl[:delkans-1]==(slovo):# neznameslovosl[:delkans-1] toto odstrani znak noveho radku po funkci readline
                  pomoc3=True #Pokud nezname slovo najde ve slovniku zmeni na true
                  projektnez=open('Projekty/'+projekt+'/Neprelozitelna slova.txt','a')
                  projektnez.write(slovo+'\n')
                  projektnez.close()
                  #print('2 ',pomoc3)
            neznameslovosl=neznameslovo.readline()#nacte dalsi radku
            delkans=len(neznameslovosl)#zjisti delku slova
      neznameslovo.close()#uzavreni souboru

      if pomoc3==False:    
            return 1#pocetslov=pocetslov+1
      else:
            return 0
    

def rozpracovane(): #funkce pro menu Projekty/Rozpracovane-vytvori seznam rozpracovanych projektu
    def dodelatprojekt():#zjisti jaky projekt je vybrany
        if seznamrozpracovane.curselection()==() :#pokud neni nic vybrane tak se vrati na vyber
            return
        projekt=seznamrozpracovane.get(seznamrozpracovane.curselection())
        vycistihlavniramec()#vycisti hlavni ramec
        vytvor_seznam2('Projekty/'+projekt+'/'+projekt+'-orig.txt',projekt)    
    vycistihlavniramec()#vycisti ramec
    stitekrozpracovane=Label(hlavniramec,text="Rozpracovane")#vytvori Label
    stitekrozpracovane.grid(row=0,column=0)#robrazi label
    seznamrozpracovane=Listbox(hlavniramec)#vytvori Listbox seznam rozpracovanych projektu
    seznamrozpracovane.grid(row=1, column=0)#robrazi Listbox
    for projekty in os.listdir('Projekty'):#prohleda slozku s projekty 
        init=open('Projekty/'+projekty+'/init','r')#otevre soubor init
        if init.readline()=='nekompletni':#kdyz je na prvni radce text nekompletni tak vlozi do Listboxu
            seznamrozpracovane.insert(END,projekty)#vlozi do Listboxu
        init.close()#zavre soubor close
    if seznamrozpracovane.get(0)!='':#pokud neni seznam prazdny zobrazi tlacitko
        tlzobraz=Button(hlavniramec, text='Dodelat projekt',command=dodelatprojekt)#vytvori Button
        tlzobraz.grid(row=1, column=1)#zobrazi Button
            
    
def vycistihlavniramec():#Vymaze vsechny widgety z Frame hlavniramec
    for widget in hlavniramec.winfo_children(): #.winfo_children()-zjisti jmena potomku ve widgetu
        widget.destroy()#.destroy() - vymaze widget

    
############################################################################

hlavniramec=Frame(root)#vytvori Frame ve kterem se boudou zapisovat dalsi Widgety
hlavniramec.grid()#zobrazi Frame
for x in range(60):
    Grid.columnconfigure(hlavniramec, x, weight=1)

for y in range(30):
    Grid.rowconfigure(hlavniramec, y, weight=1)
# zobrazení menu
hlavniMenu = Menu(root)#nacte widget menu

# vytvoři rozbalovací polozky menu Soubor a přidat ho k hlavnímu menu
menuSoubor = Menu(hlavniMenu, tearoff=0)
menuSoubor.add_command(label="Vytvorit novy projekt", command=Soubor_Otevrit)
#menuSoubor.add_command(label="Uložit", command=hello)
menuSoubor.add_separator()
menuSoubor.add_command(label="Chci Pryč", command=root.destroy)#vypne program
hlavniMenu.add_cascade(label="Soubor", menu=menuSoubor)


# další rozbalovací polozky menu Projekty
menuProjekty = Menu(hlavniMenu, tearoff=0)
menuProjekty.add_command(label="Kompletne hotove", command=Kompletne_hotove)
menuProjekty.add_command(label="Rozpracovane", command=rozpracovane)
#menuProjekty.add_command(label="Vytvorit Novy", command=hello)
hlavniMenu.add_cascade(label="Projeky", menu=menuProjekty)

# další rozbalovací polozky menu Slovniky ZATIM vypnuto
#menuSlovniky = Menu(hlavniMenu, tearoff=0)
#menuSlovniky.add_command(label="Znama slova", command=hello)
#menuSlovniky.add_command(label="Neznama slova", command=hello)
#menuSlovniky.add_command(label="Vytvorit Novy", command=hello)
#hlavniMenu.add_cascade(label="Slovniky", menu=menuSlovniky)

def oprogramu():#netreba koment
    vycistihlavniramec()#vycisti hlavni soubor
    t1='Verze 0.2.alfa.\nTento program slouzi pro vyhledani slov z titulku a jejich rucni rozrazeni do skupin: Znama slova, neznama a neprelozitelna slova\n'
    t2='Pri hledani slov v souboru zkontroluje jestli uz slova nejsou zarazena do slovniku znamych nebo neznamych slov, aby \nnedochazelok opakovanemu razeni jiz rozrazenych slov' 
    text=t1+t2
    popis=Label(hlavniramec,text=text)
    popis.grid()
# další rozbalovací polozky menu O programu
#menuSlovniky = Menu(hlavniMenu, tearoff=0)
#menuSlovniky.add_command(label="Znama slova", command=hello)
#menuSlovniky.add_command(label="Neznama slova", command=hello)
#menuSlovniky.add_command(label="Vytvorit Novy", command=hello)
hlavniMenu.add_cascade(label="O programu", command=oprogramu)

# zobrazení menu
root.config(menu=hlavniMenu) #zobrazi Hlavni menu


root.mainloop()#hlavni smycka

