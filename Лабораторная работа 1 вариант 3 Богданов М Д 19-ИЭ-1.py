from tkinter import *

root = Tk()
root.geometry('400x180')
root['bg'] = 'pink'
root.title('Богданов Максим 19-ИЭ-1')
root.resizable(0,0)

point = 0

lst5 = list('.,!?;:-()<>')
x = 0

def change():
    global point, lst, x
    vvod['state'] = 'normal'
    point = dlina.get()
    vvod.delete(0,END)
    metka['text'] = metka['text'] + x
    x = 0

def obr(event):
    global point,x, num
    lst = list(vvod.get()) # для проверки последнего символа
    try:
        if lst[0] != [] :
            lastSim = ord(lst[len(lst)-1])
            
    except:
            return 0    
    
    delete = 1   
    if point == 5:
        
        for i in range(len(lst5)):
                for j in range(len(lst)):
                        if delete == 1:
                                if lst[len(lst)-1] == lst5[i] and len(vvod.get()) <= 5:
                                        delete = 0
                                else:
                                        delete = 1
    elif point == 10:
            
        if (lastSim >= 48 and lastSim <= 57) and \
           len(vvod.get()) <= 10:
                delete = 0
                x = int(vvod.get())
        else:
                delete = 1

    elif point == 15:
            
        if (lastSim >= 65 and lastSim <= 90 or \
           lastSim >= 97 and lastSim <= 122 or \
           lastSim >= 1040 and lastSim <= 1103) and \
           len(vvod.get()) <= 15:
                delete = 0
        else:
                delete = 1

    elif point == 20:
        if (lastSim >= 65 and lastSim <= 90 or \
           lastSim >= 97 and lastSim <= 122 or \
           lastSim >= 1040 and lastSim <= 1103 or \
           lastSim >= 48 and lastSim <= 57) and \
           len(vvod.get()) <= 20:
                delete = 0
                try:
                    x = int(vvod.get())
                except:
                    x = 0
        else:
                delete = 1

    if delete == 1:
            vvod.delete(len(vvod.get())-1)
        

vvod = Entry(width = 52, state = 'disabled') #Поле Entry
vvod.place(x = 40, y = 45)
vvod.bind('<KeyRelease>', obr)
vvod.bind('<KeyPress>',obr)

metka = Label(text = 0) #Метка metka
metka.place(x = 185, y = 80)

dlina = IntVar()
dlina.set(0)

close = Button (text = 'Close', command = root.destroy)
close.place(x = 355, y = 5)

d5 = Radiobutton(text = '5sim', variable = dlina, value = 5, command = change)
d10 = Radiobutton(text = '10sim', variable = dlina, value = 10, command = change)
d15 = Radiobutton(text = '15sim', variable = dlina, value = 15, command = change)
d20 = Radiobutton(text = '20sim', variable = dlina, value = 20, command = change)

d5.place(x = 30+10, y = 120)
d10.place(x = 110+10, y = 120)
d15.place(x = 200+10, y = 120)
d20.place(x = 290+10, y = 120)

root.mainloop()
