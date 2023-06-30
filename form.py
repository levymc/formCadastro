from tkinter import *
from tkinter import messagebox
import sqlite3, hashlib


class Cadastro(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro")
        self.geometry("260x160")
        self.configure(bg="white")
        self.resizable(0,0)
        self.campos()
        
    def campos(self):        
        self.loginLabel = Label(self, text="Usuário: ", bg="white")
        self.loginLabel.place(x = 10, y = 20)
        self.login = StringVar()
        self.login = Entry(self, textvariable = self.login, bg = "white")
        self.login.place(x = 70, y = 20, width = 140)
        
        self.passwordLabel = Label(self, text="Senha: ", bg="white")
        self.passwordLabel.place(x = 10, y = 50)
        self.password = StringVar()
        self.password = Entry(self, textvariable = self.password, show='*', bg = "white")
        self.password.place(x = 70, y = 50, width = 140)
        
        self.codigoLabel = Label(self, text = "Código: ", bg = "white")
        self.codigoLabel.place(x = 10, y = 80)
        self.codigo = StringVar()
        self.codigo = Entry(self, textvariable = self.codigo, bg = "white")
        self.codigo.place(x = 70, y = 80, width = 140)
        
        submit = Button(self, text = "Cadastro", fg = "white", bg = "black", width = 10)
        submit.bind('<Button-1>', self.insere)
        submit.place(x = 160, y = 110)
        self.bind('<Return>', self.insere)
        
        self.mainloop()
    
    def insere(self, event):
        login = self.login.get()
        password = self.password.get()
        codigo = self.codigo.get()
        passwordCod = hashlib.md5(password.encode()).hexdigest()
        print(login, password, passwordCod, codigo)
        try:
            banco = sqlite3.connect(r'fpq_status.db')
            cursor = banco.cursor()
            cursor.execute(f"""
                            INSERT INTO operadores 
                            (codigo, usuario, senha, priority)
                            VALUES ('{codigo}', '{login}', '{password}', 'admin')
                            """)
            banco.commit()
            messagebox.showinfo(message="Cadastro Realizado!")
            cursor.close()
            banco.close()
        except Exception as e:
            print(e)
            messagebox.showerror(message="Algum erro aconteceu.") 
        
if __name__ == "__main__":
    app = Cadastro()
    app.mainloop()
        