from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

screen = Tk()
screen.configure(background='white')
cart={}

def Window2():
    def addtocart(item):
        item = item[0:4]
        quan = int(quantity.get())
        if item in cart.keys():
            for it,qu in cart.items():
                if it == item:
                    qu = qu + quan
        else:
            pass
            #cart[item]=quan
        print (cart)


    popup = Toplevel(screen)
    popup.title("Window 2")
    popup.configure(background='red')

    Label(popup, text="Menu Selection").pack()

    Tabs = Notebook(popup, width=600)
    Tabs.pack()

    Starter = Frame(Tabs, borderwidth=10)
    Tabs.add(Starter, text="Starters")

    MainCourse = Frame(Tabs,borderwidth=10)
    Tabs.add(MainCourse, text="Main Course")

    Dessert = Frame(Tabs, borderwidth=10)
    Tabs.add(Dessert, text="Dessert")


    ###### Starters

    Label(Starter,text="Starters").pack()
    starters = {'Garlic Bread':15,'Mozzerella Sticks':10,'Caeser Salad':20}
    for item,price in starters.items():
        text = StringVar()
        menu_item = f'{item}:{price}$'

        Label(Starter,text=menu_item).pack()
        quantity = Entry(Starter,style='TEntry')
        quantity.pack()
        Button (Starter,text='add to cart',command=lambda: addtocart(menu_item)).pack()

    ###### Main Course

    Label(MainCourse, text="Main Course").pack()

    mcourse = {'Pesto Penne': 45, 'Margherita Pizza': 55, 'Mushroom Risotto': 50}
    for item, price in mcourse.items():
        text = (f'{item}: {price}$')
        Label(MainCourse, text=text).pack()

    ###### Desserts

    Label(Dessert, text="Desserts").pack()
    desserts = {'Red Velvet Cake': 25, 'Brownie with Icecream': 30, 'Chocolate Mousse': 20}
    for item, price in desserts.items():
        text = (f'{item}:{price}$')
        Label(Dessert, text=text).pack()


myimg = Image.open('project.png')
myimg = myimg.resize((100,100))
myimg = ImageTk.PhotoImage(myimg)

label = Label(screen, image=myimg)
label.grid(row=1,column=0)



Button(screen,text="Click Me",command=Window2).grid(row=10,column=0)

screen.mainloop()