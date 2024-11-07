from tkinter import *
import matplotlib.pyplot as m 
import tkinter.messagebox

window = Tk()
window.geometry("1920x1080")
window.title("Home page")

fn = StringVar()
ln = StringVar()

#to exit out of the widget
def exit1():
    exit()
    
d_up = {"Akshita":"py$23", "Haritha":'py$22', "Tanvi":'py$14'}

def climate():
    window4 = Tk()
    window4.geometry("1920x1080")
    window4.title("Climatic Conditions")
    
def tech():
    window5 = Tk()
    window5.geometry("1920x1080")
    window5.title("New Technologies")

def second_win():
    #Authentication
    name1 = fn.get()
    pwd1 = ln.get()
    
    if (name1 in d_up) and (d_up[name1] == pwd1):
        tkinter.messagebox.showinfo("Welcome!", "The user has successfully logged in!!")
    elif (name1 in d_up) and (d_up[name1] != pwd1):
        tkinter.messagebox.showinfo("Try Again.", "Incorrect password, try again.")
    elif (len(name1) != 0) and (len(pwd1) >= 4) and (name1 not in d_up):
        d_up1 = {name1:pwd1}
        d_up.update(d_up1)
        tkinter.messagebox.showinfo("Welcome!", "The user has successfully Signed up!!")
    elif (len(name1) != 0) and (len(pwd1) < 4) and (name1 not in d_up):
        tkinter.messagebox.showinfo("Try Again!", "Please enter a password with atleast 4 characters.")
    elif (len(name1) == 0) and (len(pwd1) == 0):
        tkinter.messagebox.showinfo("Try Again.", "Please enter the user credentials for validation.")
    elif (len(name1) == 0) and (len(pwd1) != 0):
        tkinter.messagebox.showinfo("Try Again.", "Please enter the user name for validation.")
    elif (len(name1) != 0) and (len(pwd1) == 0):
        tkinter.messagebox.showinfo("Try Again.", "Please enter the password for validation.")

    #Proceeding further only after validation.
    if (name1 in d_up) and (d_up[name1] == pwd1):
        window2 = Tk()
        window2.geometry("1920x1080")
        window2.title("Choose an option")
        label3 = Label(window2, text = "Choose an option from the following: ", font = ("calibri", 30, "italic"))
        label3.place(x=100, y = 30)

        def trend(event):
            myLabel = Label(window2, text = clicked.get())#.pack(padx=100, pady=200)
            #myLabel.place(x=100, y=200)
            if clicked.get() == "Rice":
                label1 = Label(window2, text = "Rice - Profits observed, suitable for growth.", font = ("calibri",15, "italic"))
                label1.place(x=100, y=280)
                x = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
                y = [109698, 112760, 116480, 118870, 124370, 130290, 124000] 
                m.xlabel("Years") 
                m.ylabel("Production in sq. meters") 
                m.title("Crop trend in Rice")
                m.plot(x,y) 
                m.show()
                
            elif clicked.get() == "Wheat":
                label1 = Label(window2, text = "Wheat - Profits observed, suitable for growth.", font = ("calibri",15, "italic"))
                label1.place(x=100, y=320)
                x = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
                y = [87000, 98510, 99870, 103600, 107860, 109586, 103000] 
                m.xlabel("Years") 
                m.ylabel("Production in sq. meters") 
                m.title("Crop trend in Wheat") 
                m.plot(x,y) 
                m.show()
                
            elif clicked.get() == "Cotton":
                label1 = Label(window2, text = "Cotton - Profits observed, suitable for growth.", font = ("calibri",15, "italic"))
                label1.place(x=100, y=360)
                x = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
                y = [27000, 29000, 26000, 28500, 27600, 24500, 27500] 
                m.xlabel("Years") 
                m.ylabel("Production in sq. meters") 
                m.title("Crop trend in Cotton") 
                m.plot(x,y) 
                m.show() 

            elif clicked.get() == "Millet":
                label1 = Label(window2, text = "Millet - Profits observed, suitable for growth.", font = ("calibri",15, "italic"))
                label1.place(x=100, y=400)
                x = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
                y = [11560, 11640, 10236, 12489, 13208, 11700, 12000] 
                m.xlabel("Years") 
                m.ylabel("Production in sq. meters") 
                m.title("Crop trend in Millet") 
                m.plot(x,y) 
                m.show() 

            elif clicked.get() == "Coconut Oil":
                label1 = Label(window2, text = "Coconut Oil - Profits observed, suitable for growth.", font = ("calibri",15, "italic"))
                label1.place(x=100, y=440)
                x = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
                y = [446, 481, 474, 474, 474, 474, 476] 
                m.xlabel("Years") 
                m.ylabel("Production in sq. meters") 
                m.title("Crop trend in Coconut Oil") 
                m.plot(x,y) 
                m.show() 

            elif clicked.get() == "Barley":
                label1 = Label(window2, text = "Barley - Profits observed, suitable for growth.", font = ("calibri",15, "italic"))
                label1.place(x=100, y=480)
                x = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
                y = [1438, 1747, 1781, 1633, 1720, 1656, 1400] 
                m.xlabel("Years") 
                m.ylabel("Production in sq. meters") 
                m.title("Crop trend in Barley") 
                m.plot(x,y) 
                m.show() 

            elif clicked.get() == "Corn":
                label1 = Label(window2, text = "Corn - Profits observed, suitable for growth.", font = ("calibri",15, "italic"))
                label1.place(x=100, y=520)
                x = [2016, 2017, 2018, 2019, 2020, 2021, 2022] 
                y = [25900, 28753, 27715, 28766, 31647, 33600, 32000] 
                m.xlabel("Years") 
                m.ylabel("Production in sq. meters") 
                m.title("Crop trend in Corn") 
                m.plot(x,y) 
                m.show()
                
        list_crop = ["Rice", "Wheat", "Cotton", "Millet", "Coconut Oil", "Barley", "Corn"] 
        clicked = StringVar()
        clicked.set(list_crop[1])
        
        label3 = Label(window2, text = "Choose the crop for which trends have to be identified: ", font = ("calibri", 15, "italic"))
        label3.place(x=70, y = 200)  

        droplist = OptionMenu(window2, clicked, *list_crop, command = trend)
        droplist.config(width = 25)
        droplist.place(x = 100, y=240)

        button2 = Button(window2, text = "Trend Analysis:", fg = "black", bg = "green", relief = "groove", font = ("sougue", 20, "italic"), bd = 2, command = trend)
        button2.place(x=100, y=120)

        button3 = Button(window2, text = "Climatic Analysis:", fg = "black", bg = "yellow", relief = "groove", bd = 2, font = ("sougue", 20, "italic"), command = climate)
        button3.place(x=600, y=120)

        button4 = Button(window2, text = "New technologies:", fg = "black", bg = "pink", relief = "groove", bd = 2, font = ("sougue", 20, "italic"), command = tech)
        button4.place(x=1000, y=120)

        button5 = Button(window2, text = "Logout",fg = "white", bg = "brown", relief = "raised", font = ("arial", 20, "italic"), command = exit1)
        button5.place(x = 1400, y = 30)



label0 = Label(window, text = "AGRICULTURAL MANAGEMENT \n SYSTEM (AMS)", fg = "black", relief = "groove", bd = 2, font = ("calibri", 50, "bold"))
label0.place(x = 350, y = 170)

label1 = Label(window, text = "WELCOME!!", fg = "pink", font = ("sougue", 70, "bold"))
label1.place(x = 510, y = 50)

label2 = Label(window, text = "Name:", font = ("arial", 20))
label2.place(x = 510, y = 400)

entry_1 = Entry(window, textvar = fn)
entry_1.place(x = 650, y = 410)

label3 = Label(window, text = "Password:", font = ("arial", 20))
label3.place(x = 510, y = 450)

entry_2 = Entry(window, textvar = ln, show = "*")
entry_2.place(x = 650, y = 460)


button1 = Button(window, text = "Submit",fg = "white", bg = "brown", relief = "raised", font = ("arial", 20, "italic"), command = second_win)
#window.bind("<Return>", database)
button1.place(x = 620, y = 550)

#use pillow for images - import PIL
