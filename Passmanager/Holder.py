win = tk.Tk()

home_frame = tk.Frame(win)
add_frame = tk.Frame(win)
get_frame = tk.Frame(win)

for frame in (home_frame, add_frame, get_frame):
    frame.grid(row=0, column=0, sticky='news')

win.geometry('600x400')
win.minsize(400, 400)
win.title('Password manager')
menu = tk.Menu(win)
filemenu = tk.Menu(menu, tearoff = 0)
win.config(menu=menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Add New Password')
filemenu.add_command(label='Get Password')
filemenu.add_command(label='Exit', command=win.quit)
add_button = tk.Button(home_frame,
                   text = 'Add a new password',
                   activebackground="blue", 
                   activeforeground="white",
                   anchor= 'center',
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
add_button.pack(padx=20, pady=30)

get_button = tk.Button(home_frame,
                   text = 'Get a stored password',
                   activebackground="blue", 
                   activeforeground="white",
                   anchor= 'center',
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
get_button.pack(padx=20, pady=60)

home_frame.tkraise()