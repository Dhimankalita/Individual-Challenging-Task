from tkinter import *
import tkinter
import tkinter.messagebox as mb
from tkinter import filedialog


root=Tk()
root.geometry("740x600")
root.resizable(0,0)
root.title("Computer Science Project")
# Function 
def crops():
    global weather
    if not locentry.get():
     mb.showerror('Field empty!', "Please fill  the missing field !")
    else:
        weather=locentry.get()
        if weather.lower()=="hot"or weather.lower()=="summer" or weather.lower()=="dry":
            Label(outputframe,text="These crops, often referred to as warm-season or kharif crops,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
            Label(outputframe,text="require ample sunlight and warm soil temperatures",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
            Label(outputframe,text="to grow and produce a bountiful harvest.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
            Label(outputframe,text="The suitable crops that you can grow in Hot weather are:",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
            Label(outputframe,text="Vegetable- Okra, Brinjal, Sweet Potatoes, Cucumber, Green beans.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
            Label(outputframe,text="Grains and Legumes- Rice,Bajra, Sweet Corn , Cowpeas.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
            Label(outputframe,text="Herbs and Others- Basil, Tobacco, Sugarcane, Jute ,Cotton.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)

        elif weather.lower()=="cold" or weather.lower()=="winter" or weather.lower()=="snow":
            Label(outputframe,text="These crops, often referred to as winter-season or Rabi crops,",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
            Label(outputframe,text="in places like India, and many become even sweeter after a light frost. ",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
            Label(outputframe,text="The suitable crops that you can grow in Cold weather are:",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
            Label(outputframe,text="Vegetable- Broccoli, Cabbage, Cauliflower, Carrots, Lettuce.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
            Label(outputframe,text="Grains and Legumes- Wheat,Barley, Oats , Chickpeas, Lentils.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
            Label(outputframe,text="Others- Garlic, Mustard.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)



        elif weather.lower()=="rainy" or weather.lower()=="monsoon" or weather.lower()=="moist" or weather.lower()=="wet" :
            Label(outputframe,text="Crops grown in rainy weather are generally known as monsoon crops",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=360)
            Label(outputframe,text="These crops require substantial water and thrive in hot, humid conditions. ",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=390)
            Label(outputframe,text="and thrive in hot, humid conditions. ",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=420)
            Label(outputframe,text="The suitable crops that you can grow in Rainy weather are:",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=450)
            Label(outputframe,text="Vegetable and Fruits- Bitter Gourd (Karela), Bottle Gourd(Lauki),",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=480)
            Label(outputframe,text="Mango, banana, and guava.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=510)
            Label(outputframe,text="Grains and Legumes- Soybean, Black gram, Green gram, Groundnut.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=540)
            Label(outputframe,text="Others- Cotton, Sugarcane.",font=('Helvetica', 14),bg="blue", fg="yellow").place(x=80,y=570)




#Frames
inputframe=LabelFrame(root,width=630,height=150,bg="yellow").place(x=75,y=100)
outputframe=LabelFrame(root,width=630,height=300,bg="blue").place(x=75,y=300)

#Labels
hdlbl=Label(root,text="Weather Based Crop Predictor",fg="red",font=('Helvetica', 22, 'bold'),padx=0,pady=0).place(x=165,y=50)
loclabel=Label(inputframe,text="Enter the weather:",fg="blue",bg="yellow",font=('Helvetica', 20, 'bold'),padx=0,pady=0).place(x=240,y=120)
locentry=Entry(inputframe,width=25)
locentry.place(x=270,y=190)
outlabel=Label(outputframe,text="Farming Suggestion",fg="yellow",bg="blue",font=('Helvetica', 20, 'bold'),padx=0,pady=0).place(x=90,y=320)

weather=StringVar()

#Button
farmsuggbtn=Button(root,text="Get Crop Suggestion",width=20,bg="green",command=crops,height=2).place(x=275,y=255)

root.mainloop()
