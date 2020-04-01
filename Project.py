from tkinter import *
from tkinter.ttk import *
#from PIL import ImageTk, Image

screen = Tk()
screen.configure(background='white')
cart={}

def Window2():
    def addtocart():
        item = cmbvar.get()
        quan = int(quantity.get())
        print(item)
        print(quan)
 

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
    
    menu_item=StringVar(Starter)
    menu_item.set([key for key in starters][0])
    Combo1=Combobox(Starter,height=10,width=25,values=[key for key in starters],textvariable=menu_item) #Height refers to number of values it will list without scroll
    Combo1.pack()
        
    quantity=StringVar(Starter)       
    SpinBox1=Spinbox(Starter,width=10,from_=1,to=10,increment=1,textvariable=quantity) # Always Stores Values as Text
    SpinBox1.pack()
    
    btn=Button (Starter,text='add to cart',command = addtocart)
    btn.pack()

    ###### Main Course

    Label(MainCourse, text="Main Course").pack()

    mcourse = {'Pesto Penne': 45, 'Margherita Pizza': 55, 'Mushroom Risotto': 50}
    
    ###### Desserts

    Label(Dessert, text="Desserts").pack()
    desserts = {'Red Velvet Cake': 25, 'Brownie with Icecream': 30, 'Chocolate Mousse': 20}
    

# myimg = Image.open('project.png')
# myimg = myimg.resize((100,100))
# myimg = ImageTk.PhotoImage(myimg)

# label = Label(screen, image=myimg)
# label.grid(row=1,column=0)



Button(screen,text="Click Me",command=Window2).grid(row=10,column=0)

screen.mainloop()# Write your code here :-)
