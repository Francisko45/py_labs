import tkinter as tk
import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('shop_database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               firstname TEXT,
                               secondname TEXT,
                               address TEXT)''')
        self.conn.commit()

    def selectAllUsers(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def insertUser(self, firstname, secondname, address):
        self.cursor.execute("INSERT INTO users (firstname, secondname, address) VALUES (?, ?, ?)",
                            (firstname, secondname, address))
        self.conn.commit()

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.db = DB()  
        self.init_main()

    def init_main(self):
        self.toolbar = tk.Frame(self, bg="snow2", bd=1)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        add_button = tk.Button(self.toolbar, text="Додати користувача", command=self.open_add_dialog)
        add_button.pack(side=tk.LEFT)
        self.treeUser = tk.Listbox(self, height=15, width=50)
        self.treeUser.pack(side=tk.TOP)
        self.view_record_users()

    def view_record_users(self):
        users = self.db.selectAllUsers()
        self.treeUser.delete(0, tk.END)  
        for user in users:
            self.treeUser.insert(tk.END, f"ID: {user[0]}, Ім'я: {user[1]}, Прізвище: {user[2]}, Адреса: {user[3]}")

    def open_add_dialog(self):
        WindowInputDialog(self)

class WindowInputDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = parent.db 
        self.init_input()

    def init_input(self):
        self.title("Додати нового користувача")
        self.geometry("300x200+300+170")
        self.resizable(False, False)
        label_name = tk.Label(self, text="Ім'я")
        label_name.pack()
        self.entry_name = tk.Entry(self)
        self.entry_name.pack()
        label_secondname = tk.Label(self, text="Прізвище")
        label_secondname.pack()
        self.entry_secondname = tk.Entry(self)
        self.entry_secondname.pack()
        label_address = tk.Label(self, text="Адреса")
        label_address.pack()
        self.entry_address = tk.Entry(self)
        self.entry_address.pack()
        btn_cancel = tk.Button(self, text="Відмінити", command=self.destroy)
        btn_cancel.pack(side=tk.LEFT, padx=20)
        btn_add = tk.Button(self, text="Додати", command=self.add_data)
        btn_add.pack(side=tk.LEFT)

    def add_data(self):
        self.db.insertUser(self.entry_name.get(),
                           self.entry_secondname.get(),
                           self.entry_address.get())
        self.entry_name.delete(0, 'end')
        self.entry_secondname.delete(0, 'end')
        self.entry_address.delete(0, 'end')
        self.destroy() 

if __name__ == "__main__":
    root = tk.Tk()
    root.title("База даних користувачів")
    root.geometry("400x400")
    app = Main(root)
    app.pack()
    root.mainloop()
