"""All rights are Reserved 
    Varun Arora
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
from bubblesort import bubbleSort
from quicksort import quickSort
from selectionsort import selectionSort
from insertionsort import insertionSort
data = []
speed_value = float()
    
def draw_bars(data: list, colorarray):
    canva.delete("all")
    canva_height = 600
    canva_width = 1000
    width_of_bar = canva_width/len(data) + 1
    offset = 10
    spacing_bar = 4
    normalised_data = [i/max(data) for i in data]
    
    
    for i, height in enumerate(normalised_data):
        x0 = i*width_of_bar + offset + spacing_bar
        y0 = canva_height - height * 400
        
        x1 = (i+1)* width_of_bar
        y1 = canva_height
        
        
        
        canva.create_rectangle(x0, y0, x1, y1, fill = colorarray[i])
        canva.create_text(x0+2, y0, anchor= SW,
                           text= str(data[i]),
                           font = ('monospace', 15, 'bold'),
                           fill = 'purple')
        window.update_idletasks()
        
def click(x: str):
    messagebox.showinfo(message=f"You Selected {x} Algorithm")
def new_arr():
    global data, speed_value
    
    #displaying selected algorihm
    click(algo_menu.get())
   
    #getting values
    try :
        min_value = int(min_entry.get())
    except: #if input value is wrong then we will use default min as 1
        min_value = 1
        
    try :
        max_value = int(max_entry.get())
    except:
        max_value = 100
        
    try :
        size_value = int(size_entry.get())
    except:
        size_value = 5
        
    speed_value = speed_scale.get()

    if speed_value == "":
        speed_value = 0.01
    elif float(speed_value) > 2:
        speed_value = 0.01
    else:
        speed_value = float(speed_value)
        
    if min_value < 0:
        min_value = 0
    if max_value> 1000:
        max_value = 100
    if size_value > 20 or size_value < 3:
        size_value = 5
    
        
    #if in case max_value is less than min_value then swap max_value and min_value
    
    if max_value < min_value:
        max_value , min_value = min_value, max_value
        
    data= []
    
    for j in range(size_value):
        data.append(random.randrange(min_value, max_value + 1))
        
    draw_bars(data, ['#00FCEA'  for i in range(len(data))])
    
def Sort():
     global data, speed_value
     if not data:
         return
     
     if(algo_menu.get() == "Quick Sort"):
            quickSort(data, 0, len(data)-1, draw_bars, float(speed_value))
            draw_bars(data, ['#003153' for x in range(len(data))] )
     elif(algo_menu.get() == "Bubble Sort"):
        bubbleSort(data, draw_bars, speed_value)
     elif(algo_menu.get()=="Selection Sort"):
         selectionSort(data, draw_bars, speed_value)
     elif(algo_menu.get()=="Insertion Sort"):
         insertionSort(data, draw_bars, speed_value)


    
window = Tk()
window.title('Sorting visualizer')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry(f'{width}x{height}')
window.config(bg='#00FCEA')

heading = Image.open('image.png')
heading = heading.resize((480,120))
heading = ImageTk.PhotoImage(heading)

heading_label = Label(window, image=heading)

mainlabel = Label(window, 
                  text='Select Algorithms: ',
                  font=("Monospace", 18, "bold"),
                  bg='#000107',
                  fg='#EDF4F2',
                  relief= 'solid',
                  padx=1,
                  pady=6
                  )

new_array = Button(window, text='New Array', 
                   font=("Monospace", 18, "bold"), 
                   bg='#000107',fg='#EDF4F2', 
                   relief= 'groove', 
                   command = new_arr,
                   padx=1, pady=4, bd = 5
                   )

selected_algo = StringVar()
algo_menu = ttk.Combobox(window, 
                         font=("Monospace", 24, "bold"),
                         background='#EDF4F2',
                         foreground='#000107',
                         textvariable=selected_algo,
                         values = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Quick Sort"],
                         width=12)

sizelabel = Label(window, text="Size: ",
                  font=("Monospace", 18, "bold"),
                  bg='#000107',
                  fg='#EDF4F2',
                  relief= 'solid',
                  padx=1,
                  pady=6)

size_entry = Entry(master=window,
           font=('monospace',27,'bold'),
           bg='#EDF4F2',
           fg='#000107',
           width=8)

minlabel = Label(window, text="Min value: ",
                  font=("Monospace", 18, "bold"),
                  bg='#000107',
                  fg='#EDF4F2',
                  relief= 'solid',
                  padx=1,
                  pady=6)

min_entry = Entry(master=window,
           font=('monospace',27,'bold'),
           bg='#EDF4F2',
           fg='#000107',
           width=8)

maxlabel = Label(window, text="Max Value: ",
                  font=("Monospace", 18, "bold"),
                  bg='#000107',
                  fg='#EDF4F2',
                  relief= 'solid',
                  padx=1,
                  pady=6)

max_entry = Entry(master=window,
           font=('monospace',27,'bold'),
           bg='#EDF4F2',
           fg='#000107',
           width=8)

speed = Label(window, text='Delay: ',
              bg='#000107',
                  fg='#EDF4F2',
                  relief= 'raised',
                  padx=1,
                  pady=6,
                font=("Monospace", 18, "bold"),
              )

speed_scale = Entry(window,
                    font=("Monospace", 27, "bold"),
                  fg='#000107',
                  bg='#EDF4F2',
                  width=8
                    )

sort = Button(window, text="Sort",
              relief=GROOVE,
              font=("Monospace", 18, "bold"), 
                   bg='#000107',fg='#EDF4F2',
             padx=1, pady=4, bd = 5,
             command = Sort
              )

canva = Canvas(window,
               width=1020,
               height=600,
               bg='#000107')
exit = Button(window,
              text="Exit",
              relief=GROOVE,
              command= window.destroy,
              font=("Monospace", 12, "bold"), 
                   bg='#000107',fg='#EDF4F2',
             padx=1, pady=4, bd = 5
              )

algo_menu.current(0) #Initial menu choice

#placing all the widgets elements
heading_label.place(x= 550, y = 5)
new_array.place(x= 30,y= 150)
sizelabel.place(x= 235, y = 150)
size_entry.place(x = 310, y = 150)
minlabel.place(x = 560, y = 150)
min_entry.place(x = 699, y = 150)
maxlabel.place(x =960, y = 150)
max_entry.place(x= 1105, y = 150)
mainlabel.place(x=1040, y= 270)
algo_menu.place(x=1270, y=270)
speed.place(x= 1040, y = 400)
speed_scale.place(x= 1140, y = 400)
sort.place(x = 1040, y = 470)
canva.place(x = 10, y = 270)
exit.place(x= 1470, y = 830)
window.mainloop()
