import tkinter as tk
from tkinter import * 
import Login
import search
class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs, className= " Netflix Titles")
        #window creation
        #self.window.resizable(width=False, height=False)
        #frame creation
        #self.configure(bg = "light green")

        photo = PhotoImage(file = 'netflix_icon.png')
        self.iconphoto(False, photo)
        frame1 = tk.Frame(self)
        frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand = True)
        frame1.pack_propagate(False)

        frame1.grid_rowconfigure(0, weight = 1)
        frame1.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}

        for F in (LoginPage, Page1):
  
            frame = F(frame1, self)

            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_page(LoginPage)

    def show_page(self, page):
        frame = self.frames[page]
        frame.tkraise()
        


    
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = "black")
        #Welcome text creation
        self.welcome_Text = tk.Label(self, text="WELCOME TO NETFLIX TITLES", font=("Bahnschrift Light SemiCondensed", 30), bg= "Black", fg = "Red")
        self.welcome_Text.place(relx = 0.5, rely = 0.20, anchor ='center') 
        #Username, textbox creation and input
        self.name = tk.StringVar()
        self.userName_label = tk.Label(self, text="Username:",font= ("Bahnschrift Light SemiCondensed", 15), bg="Black", fg = "Red")
        self.userName_textbox = tk.Entry(self, width= 15, font="Arial", textvariable= self.name)

        self.userName_label.place(relx = 0.35, rely = 0.40, anchor= 'center')
        self.userName_textbox.place(relx = 0.55, rely = 0.40, anchor ='center') 
        #Upassword, textbox creation and input
        self.password = tk.StringVar()
        self.password_label = tk.Label(self, text="Password:",font= ("Bahnschrift Light SemiCondensed", 15), bg="Black", fg = "Red")
        self.password_textbox = tk.Entry(self, width= 15, font="Arial", textvariable=self.password, show = '*') 

        self.password_label.place(relx = 0.35, rely = 0.50, anchor= 'center')
        self.password_textbox.place(relx = 0.55, rely = 0.50, anchor ='center')
    #button
        self.button = tk.Button(self, text = "Login Here!", font = ("Bahnschrift Light SemiCondensed", 15), command = lambda : self.login_button(controller))
        self.button.place(relx = 0.50, rely = 0.70, anchor ='center')
    def login_button(self, controller):
        person = Login.User()
        person.set_username(self.userName_textbox.get())
        person.set_password(self.password_textbox.get())

        
        self.result1_label = tk.Label(self, text="Login Failed", font= ("Bahnschrift Light SemiCondensed", 15), bg="Black")

        if(person.verifyLogin() == True):
            #self.result1_label = tk.Label(self, text="Login Sucessful", font= ("Bahnschrift Light SemiCondensed", 15), bg="light green")
            #self.result1_label.place(relx = 0.50, rely = 0.90, anchor ='center')
            controller.show_page(Page1)
        else:
            self.result1_label.configure(text= "  Login Failed   ", fg = "Red")
            self.result1_label.place(relx = 0.50, rely = 0.90, anchor ='center')
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = "Black")

        #Search Bar
        self.searchBar = tk.StringVar()
        self.searchBar_textbox = tk.Entry(self, width= 20, font=("Bahnschrift Light SemiCondensed", 15), textvariable= self.searchBar)
        self.searchBar_textbox.place(relx = 0.75, rely = 0.10, anchor= 'center')

        #Button
        self.button = tk.Button(self, text = "Search", font = ("Bahnschrift Light SemiCondensed", 10), height = 1, width = 6, command = lambda : self.search_button())
        self.button.place(relx = 0.93, rely = 0.10, anchor ='center')

        self.result2_label = tk.Label(self, text=" ", font= ("Bahnschrift Light SemiCondensed", 15), bg="Black")
        self.result3_label = tk.Label(self, text=" ", font= ("Bahnschrift Light SemiCondensed", 15), bg="Black")

    def search_button(self):
        result = search.Film()
        result.set_search(self.searchBar_textbox.get())

        self.result2_label = tk.Label(self, text=" ", font= ("Bahnschrift Light SemiCondensed", 15), bg="Black")
        self.result3_label = tk.Label(self, text=" ", font= ("Bahnschrift Light SemiCondensed", 15), bg="Black")
        self.result4_label = tk.Label(self, text=" ", font= ("Bahnschrift Light SemiCondensed", 15), bg="Black")

        if(result.searchInDatabase() == True):
            self.result3_label.configure(text= "   Result Found   ", fg = "Red")
            self.result3_label.place(relx = 0.50, rely = 0.90, anchor ='center')
            self.result4_label.configure(text = result.formatResult(self.searchBar_textbox.get()), fg = "Red")
            self.result4_label.place(relx = 0.50, rely = 0.55, anchor= 'center')
        else:
            self.result2_label.configure(text= "Result Not Found", fg = "Red")
            self.result2_label.place(relx = 0.50, rely = 0.90, anchor ='center')


app = UI()
app.geometry("800x500")
app.resizable(width=False, height=False)
app.mainloop()


