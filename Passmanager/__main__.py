import tkinter as tk
import PasswordLogic as pl
import PasswordGenerator as pg

class Password_UI:
    def __init__(self, root=None):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.root.geometry('500x150')
        # self.root.minsize(100, 100)
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
                   command= self.create_add_page
                   ).pack()
        tk.Button(self.frame,
                   text = 'Get a stored password',
                   command= self.create_get_page
                   ).pack()
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
        self.site = tk.Entry(self.frame)
        self.username = tk.Entry(self.frame)
        self.password = tk.Entry(self.frame)
        self.generate_random = tk.Button(self.frame, text='Generate Password', command= self.create_rand_pass)
        self.generate_random.grid(row=3, column=2)
        tk.Label(self.frame, text='Add Page').grid(row=0)
        tk.Button(self.frame, text='Go back', command=self.go_back).grid(row=4)
        self.add_button = tk.Button(self.frame, text='Add Account and Password', command= self.add_password)
        

        # Creating Layout here
        self.site.grid(row=1, column=1)
        self.username.grid(row=2, column=1)
        self.password.grid(row=3, column=1)
        self.add_button.grid(row=4,column=1)
    
    
    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.home_page()

    def create_rand_pass(self):
        rand_pass = pg.generate_password()
        # Can't make END work here for some reason, decided to grab the length of whatever text is in the entry widget
        self.password.delete(0, len(self.password.get()))
        self.password.insert(0, rand_pass)

    def add_password(self):
        pl.write_password(self.site.get(), self.username.get(), self.password.get())


class Get_Page:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Get Page by Site').grid(row=0)
        tk.Button(self.frame, text='Go back', command=self.go_back).grid(row=4)
        tk.Label(self.frame, text='Site').grid(row=1)
        tk.Label(self.frame, text='Username').grid(row=2)
        tk.Label(self.frame, text='Password').grid(row=3)
        self.site = tk.Entry(self.frame)
        self.username = tk.Label(self.frame)
        self.password = tk.Label(self.frame)
        self.get_button = tk.Button(self.frame, text='Get Username and Password', command= self.get_password)


        # Creating layout here
        self.site.grid(row=1, column=1)
        self.username.grid(row=2, column=1)
        self.password.grid(row=3, column=1)
        self.get_button.grid(row=4,column=1)

    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.home_page()

    def get_password(self):
        login_info = pl.read_password(self.site.get())
        try:
            username = login_info['username']
            password = login_info['password']
            self.username.config(text = username)
            self.password.config(text = password)
        except TypeError as e:
            self.username.config(text = "Does Not Exist")
            self.password.config(text = "Does Not Exist")

if __name__ == '__main__':
    root = tk.Tk()
    app = Password_UI(root)
    root.mainloop()