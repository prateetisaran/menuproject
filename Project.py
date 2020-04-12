from tkinter import *
from tkinter.ttk import *

# from PIL import ImageTk, Image

screen = Tk()
screen.configure(background='white')

cart ={}

def Window2():
    
    def addtocart(menu_item,qty,price):
         
        #price = [price for price in menu_item.keys() if me
        cart[menu_item] = [qty,int(qty)*int(price)]
        print(cart)
    
    def viewcart():
        displaycart = Toplevel(placeorder)
        displaycart.geometry("650x300")
        displaycart.configure(background='lightblue')
        displaycart.title("View Cart")
        
        tv = Treeview(displaycart, show='headings', columns=["Menu Item","Quantity","Price"], height=9)
     
        for col in ["Menu Item","Quantity","Price"]:
             tv.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tv, _col, False))
        tv.pack()

        for food,details in cart.items():
            tv.insert("", END, values=(food,details[0],f"AED {details[1]}"))
    
    
    placeorder = Toplevel(screen)
    placeorder.title("Window 2")
    placeorder.configure(background='red')

    Label(placeorder, text="Menu Selection").pack()

    Tabs = Notebook(placeorder, width=600)
    Tabs.pack()

    Starter = Frame(Tabs, borderwidth=10)
    Tabs.add(Starter, text="Starters")

    MainCourse = Frame(Tabs, borderwidth=10)
    Tabs.add(MainCourse, text="Main Course")

    Dessert = Frame(Tabs, borderwidth=10)
    Tabs.add(Dessert, text="Dessert")
    
    ###### Starters

    Label(Starter, text="Starters").pack()
    starters = {'Garlic Bread': 15, 'Mozzerella Sticks': 10, 
    'Caeser Salad': 20}

    print([price for (item,price) in starters.items() if item=="Garlic Bread"][0])
    starter = StringVar(Starter)
    starter.set([key for key in starters][0])
    Combo1 = Combobox(Starter, height=10, width=25, values=[key for key in starters],
                      textvariable=starter)  # Height refers to number of values it will list without scroll
    Combo1.pack()

    starter_qty = StringVar(Starter)
    SpinBox1 = Spinbox(Starter, width=10, from_=1, to=10, increment=1,
                       textvariable=starter_qty)  # Always Stores Values as Text
    SpinBox1.pack()

    btn = Button(Starter, text='add to cart', 
    command=lambda: addtocart(starter.get(),
    starter_qty.get(),
    [price for (item,price) in starters.items() if item==starter.get()][0]))
    btn.pack()
    
    btn = Button(Starter, text='View Cart', command=viewcart)
    btn.pack()
    

    ###### Main Course

    Label(MainCourse, text="Main Course").pack()

    mcourse = {'Pesto Penne': 45, 'Margherita Pizza': 55, 'Mushroom Risotto': 50}
    
    maincourse = StringVar(MainCourse)
    maincourse.set([key for key in mcourse][0])
    Combo1 = Combobox(MainCourse, height=10, width=25, values=[key for key in mcourse],
                      textvariable=maincourse)  # Height refers to number of values it will list without scroll
    Combo1.pack()

    maincourse_qty = StringVar(MainCourse)
    SpinBox1 = Spinbox(MainCourse, width=10, from_=1, to=10, increment=1,
                       textvariable=maincourse_qty)  # Always Stores Values as Text
    SpinBox1.pack()

    btn = Button(MainCourse, text='add to cart', 
    command= lambda:addtocart(maincourse.get(),
    maincourse_qty.get(),
    [price for (item,price) in mcourse.items() if item==maincourse.get()][0]))
    btn.pack()
    btn = Button(MainCourse, text='View Cart', command=viewcart)
    btn.pack()

    ###### Desserts

    Label(Dessert, text="Desserts").pack()

    desserts = {'Red Velvet Cake': 25, 'Brownie with Icecream': 30, 'Chocolate Mousse': 20}
    dessert = StringVar(Dessert)
    dessert.set([key for key in desserts][0])
    Combo1 = Combobox(Dessert, height=10, width=25, values=[key for key in desserts],
                      textvariable=dessert)  # Height refers to number of values it will list without scroll
    Combo1.pack()

    dessert_qty = StringVar(Dessert)
    SpinBox1 = Spinbox(Dessert, width=10, from_=1, to=10, increment=1,
                       textvariable=dessert_qty)  # Always Stores Values as Text
    SpinBox1.pack()

    btn = Button(Dessert, text='add to cart', 
    command=lambda:addtocart(dessert.get(),
    dessert_qty.get(),
    [price for (item,price) in desserts.items() if item==dessert.get()][0]))
    btn.pack()
    btn = Button(Dessert, text='View Cart', command=viewcart)
    btn.pack()
    


# myimg = Image.open('project.png')
# myimg = myimg.resize((100,100))
# myimg = ImageTk.PhotoImage(myimg)

# label = Label(screen, image=myimg)
# label.grid(row=1,column=0)

Button(screen, text="Click Me", command=Window2).grid(row=10, column=0)

screen.mainloop()
