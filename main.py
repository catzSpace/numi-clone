from tkinter import *
from themes.colors import *
from src.calculate import *
from src.data import *


# VENTANA PRINCIPAL

root = Tk() 
root.title("Numi Clone")
root.attributes("-topmost", True)
root['bg'] = colors['bg']
root.minsize(500, 700)  # width, height



# switch theme button
is_on = True
elements = []



# change theme 
def switch():

    global is_on

    if is_on:
        theme_button.config(text= "☾", bg = colors['fg'], fg=colors['bg'], 
                            activebackground=colors['fg'],
                            activeforeground=colors['bg'] )

        root.config(bg = colors['fg'])

        for i in elements:
            if i != output:
                i.config(bg = colors['fg'], fg = colors['bg'])
            else:
                i.config(bg = colors['fg'], fg = colors['red'])

        is_on = False

    else:
        theme_button.config(text= "☼", bg = colors['bg'], fg=colors['fg'],
                            activebackground=colors['bg'],
                            activeforeground=colors['fg'] )

        root.config(bg = colors['bg'])

        for i in elements:
            if i != output:
                i.config(bg = colors['bg'], fg = colors['fg'])
            else:
                i.config(bg = colors['bg'], fg = colors['result'])
        
        is_on = True

# data del usuario
text = ''
result = ''
linea = 1



# escaneo de la entrada
def esc(event):

    global text
    global linea
    global result

    if event.char == '\r' or event.char == '\n':
        data.update({
            linea :{
                'entrada': text,
                'salida': ''
            },
        })
        
        #print(data)
        #print(text)
        
                
        basicOperations()

        result += f'{data[linea]['salida']}\n'

        output.config(text=result)
        
        text = ''
        linea += 1

        #elif event.char == '\x08':
        #data[linea]['entrada'] = data[linea]['entrada'][:-1]
    
    else:
        if event.char == '\x08':
            text = text[:-1]
        else:
            text += event.char
        




# ELEMENTS 

title = Label(root, text='Numi Clone', 
              font=("arial", 15), bg=colors['bg'], 
              fg=colors['fg'], borderwidth=0, 
              relief="flat", highlightthickness=0)

output = Label(root, text='',
            font=("arial", 20), bg=colors['bg'],
            height=35, 
            fg=colors['result'], borderwidth=0, 
            relief="flat", highlightthickness=0)

t = Text(root, bg=colors['bg'], 
         fg=colors['fg'], height=20, 
         width=55, font=("arial", 20),
         bd=0,borderwidth=0, relief="flat", 
         highlightthickness=0)


theme_button = Button(root,text= "☼" , bg=colors['bg'], fg=colors['fg'], 
                    borderwidth=0, relief="flat",
                    activebackground=colors['bg'],
                    activeforeground=colors['fg'],
                    highlightthickness=0,
                    font=("arial", 30),
                    command = switch)


elements = [title, t, output]



title.pack(side="top", pady=10, anchor="n", fill="x")
output.pack(side="right", padx=40, fill='y')
t.pack(side="left",padx=20, pady=75, expand=True, fill='y')

t.bind("<KeyPress>", esc)

theme_button.place(relx=0.0, rely=1.0, anchor="sw", x=10, y=-10)



root.mainloop()
