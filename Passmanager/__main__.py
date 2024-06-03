import tkinter as tk
import PasswordLogic as pl

class Password_UI:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.root.geometry('600x400')
        self.root.minsize(400, 400)
        self.root.title('Password Manager')
        self.menu = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menu, tearoff = 0)
        self.root.config(menu=self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        # self.filemenu.add_command(label='Add New Password', command= self.create_add_page)
        # self.filemenu.add_command(label='Get Password', command= self.create_get_page)
        self.filemenu.add_command(label='Exit', command=self.root.quit)
        tk.Label(self.frame, text='Main Menu').pack()
        tk.Button(self.frame,
                   text = 'Add a new password',
                   command= self.create_add_page,
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
                   wraplength=100).pack()
        tk.Button(self.frame,
                   text = 'Get a stored password',
                   command= self.create_get_page,
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
                   wraplength=100).pack()
        self.add_page = Add_Page(master=self.root, app=self)
        self.get_page = Get_Page(master=self.root, app=self)

    def home_page(self):
        self.frame.pack()

    def create_add_page(self):
        self.frame.pack_forget()
        self.add_page.start_page()

    def create_get_page(self):
        self.frame.pack_forget()
        self.get_page.start_page()


class Add_Page:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Site').grid(row=1)
        tk.Label(self.frame, text='Username').grid(row=2)
        tk.Label(self.frame, text='Password').grid(row=3)
        self.site = tk.Entry(self.frame).grid(row=1, column=1)
        self.username = tk.Entry(self.frame).grid(row=2, column=1)
        self.password = tk.Entry(self.frame).grid(row=3, column=1)
        tk.Button(self.frame, text='Generate Random Password').grid(row=3, column=2)
        tk.Label(self.frame, text='Add Page').grid(row=0)
        tk.Button(self.frame, text='Go back', command=self.go_back).grid(row=4)
        tk.Button(self.frame, text='Add Account and Password', command=pl.write_password(self.site, self.username, self.password)).grid(row=4,column=1)

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.home_page()

class Get_Page:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Get Page').pack()
        tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.home_page()

if __name__ == '__main__':
    root = tk.Tk()
    app = Password_UI(root)
    root.mainloop()