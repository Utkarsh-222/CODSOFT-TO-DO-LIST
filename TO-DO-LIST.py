from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text="To-Do-List", font='ariel 25 bold', width=10, bd=5, bg='#D3D3D3', fg='black')
        self.label.pack(side='top', fill=BOTH,)

        self.label2 = Label(self.root, text="Add tasks", font='ariel 18 bold', fg='black', bg='#FFB6C1', width=10, bd=5)
        self.label2.place(x=40, y=74)

        self.label3 = Label(self.root, text="Tasks", font='ariel 18 bold', fg='black', bg='#FFB6C1', width=10, bd=5)
        self.label3.place(x=320, y=64)

        self.main_text = Listbox(self.root, height=12, width=23, bd=5, font="cursive 20  bold",bg='#AFEEEE')
        self.main_text.place(x=280, y=110)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel 11 bold',bg='#EEE8AA')
        self.text.place(x=20, y=140)

        self.button = Button(self.root, text="ADD", font='ariel 18 bold', width=10, bd=5, bg='#FF6F61', fg='black', command=self.add)
        self.button.place(x=30, y=210)

        self.button1 = Button(self.root, text="DELETE", font='ariel 18 bold', width=10, bd=5, bg='#FF6F61', fg='black', command=self.delete)
        self.button1.place(x=30, y=290)

        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.main_text.yview)
        self.scrollbar.place(x=615, y=113, height=270)

        # Connect the Scrollbar to the Listbox
        self.main_text.config(yscrollcommand=self.scrollbar.set)
    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content+"\n")
        self.text.delete(1.0, END)

    def delete(self):
        selected_item_index = self.main_text.curselection()
        if selected_item_index:
            self.main_text.delete(selected_item_index)
            with open('data.txt', 'w') as file:
                for item in self.main_text.get(0, END):
                    file.write(item+"\n")
        self.text.delete(1.0, END)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
