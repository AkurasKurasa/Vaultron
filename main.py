from tkinter import *
import random
import csv
from storage import Storage

USER = 'User'
PASSWORD = 'password'
DB = 'db.csv'
RANDOMIZED_QUESTIONS = (("Random Question #1", 1),
                     ("Random Question #2", 2),
                     ("Random Question #3", 3))


class PaC:
    def __init__(self, root):
        root.configure(bg="black")

        frame = LabelFrame(root, text="SECURITY QUESTIONS", width=400, height=150, borderwidth=2, relief="solid",
                           font=("Futura", 15, "bold"), bg="black", fg="#20C20E")

        self.password_label = Label(frame, text='PASSWORD: ', font=("Futura", 13), fg="#20C20E", bg="black")

        self.password_entry = Entry(frame, width=30, bg='white', show='*', fg="#20C20E")

        self.randomized_label = Label(frame, text='(enter random questions here)', font=('Futura', 13),
                                      fg="#20C20E", bg="black")
        self.randomized_password = Entry(frame, width=39, bg='white', fg="#20C20E")
        self.submit_button = Button(root, text='Submit', width=20, command=self._access)

        self.password_label.place(x=0, y=22, relx=0, rely=0)
        self.password_entry.place(x=85, y=20, relx=0, rely=0)
        self.randomized_label.place(x=0, y=75)
        self.randomized_password.place(x=0, y=100)
        self.submit_button.place(x=125, y=165)

        frame.pack(padx=15, pady=10)

        rand = random.randint(0, len(RANDOMIZED_QUESTIONS) - 1)
        self.randomized_label['text'] = RANDOMIZED_QUESTIONS[rand][0]
        self.random_pass = RANDOMIZED_QUESTIONS[rand][1]

    def main(self, root):

        root.configure(bg='black')
        root.title("Main Hub")

        greetings = Label(root, text=f'Hello, {USER}!', bg='black', font=('Futura', 13, 'bold'),
                               fg='#20C20E')
        ask = Label(root, text='What would you like to do?', bg='black', font=('Futura', 13, 'bold'),
                         fg='#20C20E')

        add = Button(root, text='ADD', width=20, highlightbackground='black', fg='#20C20E', font=('Futura', 10),
                     command=lambda: self._add(root))
        remove = Button(root, text='REMOVE', width=20, highlightbackground='black', fg='#20C20E', font=('Futura', 10),
                        command=lambda: self._remove(root))
        view = Button(root, text='VIEW', width=20, highlightbackground='black', fg='#20C20E', font=('Futura', 10),
                      command=lambda: self._view(root))
        search = Button(root, text='SEARCH', width=20, highlightbackground='black', fg='#20C20E', font=('Futura', 10),
                        command=lambda: self._search(root))
        update = Button(root, text='UPDATE', width=20, highlightbackground='black', padx=94, fg='#20C20E',
                        font=('Futura', 10), command=lambda: self._update(root))

        greetings.grid(column=0, row=0)
        ask.grid(column=0, row=2, columnspan=1)
        add.grid(column=0, row=3, sticky='ew')
        remove.grid(column=1, row=3, sticky='ew')
        view.grid(column=0, row=4, sticky='ew')
        search.grid(column=1, row=4, columnspan=2, sticky='ew')
        update.grid(column=0, row=5, columnspan=2, sticky='ew')

    def add(self, tp):
        tp.configure(bg='black')
        tp.title("Add account")

        ask = Label(tp, text='What would you like to add?', bg='black',
                         font=('Futura', 13, 'bold'), fg='#20C20E')

        acc_label = Label(tp, text='Account:', bg='black', font=('Futura', 10), fg='#20C20E')
        self.account = Entry(tp, width=20, highlightbackground='black', fg='#20C20E')

        pass_label = Label(tp, text='Password:', bg='black', font=('Futura', 10), fg='#20C20E')
        self.password = Entry(tp, width=20, highlightbackground='black', fg='#20C20E')

        sites_sep = Label(tp, text='(Seperate sites with " ")', bg='black', font=('Futura', 10, 'italic'),
                          fg='#20C20E')
        sites_label = Label(tp, text='Which sites can this be used?', bg='black',
                                 font=('Futura', 13), fg='#20C20E')
        self.sites = Entry(tp, width=20, highlightbackground='black', fg='#20C20E')

        submit = Button(tp, text='Submit', highlightbackground='black', width=11,
                        command=self._add_submit)

        back = Button(tp, text='Return to Menu', highlightbackground='black',
                      command=lambda: tp.destroy())

        ask.pack()

        acc_label.pack()
        self.account.pack()

        pass_label.pack()
        self.password.pack()

        sites_label.pack()
        sites_sep.pack()
        self.sites.pack()

        submit.pack()

        back.pack()

        tp.mainloop()
        
    def remove(self, tp):
        tp.configure(bg='black')
        tp.title('Remove an account')

        name = Label(tp, text='Name of the account you want to delete?', bg='black',
                          font=('Futura', 13, 'bold'), fg='#20C20E')
        self.name_entry = Entry(tp, width=30, fg='#20C20E')

        back = Button(tp, text='Return to Menu', highlightbackground='black', fg='#20C20E',
                      command=lambda: tp.destroy())
        submit = Button(tp, text='Submit', highlightbackground='black', width=11, fg='#20C20E',
                        command=self._remove_submit)

        name.pack()
        self.name_entry.pack()

        submit.pack()
        back.pack()

        tp.mainloop()
        
    def view(self, tp):
        Storage.data.clear()
        Storage.mem()
        
        tp.configure(bg='black')
        tp.title('View accounts')

        acc_label = Label(tp, text='Accounts', bg='black', font=('Futura', 13, 'bold'), fg='#20C20E')
        pass_label = Label(tp, text='Passwords', bg='black', font=('Futura', 13, 'bold'), fg='#20C20E')

        accounts = Text(tp, width=40, bg='black', highlightbackground='green', font=('Futura', 10), fg='#20C20E')
        for i in Storage.data:
            accounts.insert(END, i[0] + '\n')
        passwords = Text(tp, width=40, bg='black', highlightbackground='green', font=('Futura', 10), fg='#20C20E')
        for i in Storage.data:
            passwords.insert(END, i[1] + '\n')
        back = Button(tp, text='Return to Menu', highlightbackground='black', fg='#20C20E',
                      command=lambda: tp.destroy())

        acc_label.grid(column=0, row=0)
        pass_label.grid(column=1, row=0)
        accounts.grid(column=0, row=1)
        passwords.grid(column=1, row=1)

        back.grid(column=0, row=2)

        tp.mainloop()
        
    def search(self, tp):
        Storage.data.clear()
        Storage.mem()

        tp.configure(bg='black')
        tp.title('Search account')

        search_label = Label(tp, text='Name of websites you wish to view accounts for?',
                                  bg='black', font=('Futura', 13, 'bold'), fg='#20C20E')
        self.search_entry = Entry(tp, width=30, highlightbackground='black', fg='#20C20E')
        self.results = Text(tp, width=39, bg='black', highlightbackground='green',
                            font=('Futura', 10), fg='#20C20E')
        back = Button(tp, text='Return to Menu', highlightbackground='black',
                      command=lambda: tp.destroy())
        submit = Button(tp, text='Submit', highlightbackground='black',
                        command=self._search_submit)

        search_label.pack()
        self.search_entry.pack()
        self.results.pack()
        submit.pack()
        back.pack()

        tp.mainloop()

    def update(self, tp):
        tp.configure(bg='black')
        tp.title('Update account')

        search_acc = Label(tp, text='Search for an account', bg='black', font=('Futura', 13, 'bold'), fg='#20C20E')
        self.acc_input = Entry(tp, width=30, highlightbackground='black', fg='#20C20E')

        inquire = Label(tp, text="What do you want to change?", bg='black', font=('Futura', 13, 'bold'), fg='#20C20E')
        self.inquire_input = Entry(tp, width=30, highlightbackground='black', fg='#20C20E')

        change = Label(tp, text="Change to what?", bg='black', font=('Futura', 13, 'bold'), fg='#20C20E')
        self.change_input = Entry(tp, width=30, highlightbackground='black', fg='#20C20E')

        back = Button(tp, text='Return to Menu', highlightbackground='black',
                      command=lambda: tp.destroy())
        submit = Button(tp, text='Submit', highlightbackground='black',
                        command=self._update_submit)

        search_acc.pack()
        self.acc_input.pack()

        inquire.pack()
        self.inquire_input.pack()

        change.pack()
        self.change_input.pack()

        back.pack()
        submit.pack()
    
    def _add(self, head):
        next = Toplevel(head)
        self.add(next)

    def _add_submit(self):
        account = str(self.account.get())
        password = str(self.password.get())
        websites = str(self.sites.get()).split(' ')

        with open(DB, 'a') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows([[account, password, *websites]])

        self.account.delete(0, END)
        self.password.delete(0, END)
        self.sites.delete(0, END)

    def _remove(self, head):
        next = Toplevel(head)
        self.remove(next)

    def _remove_submit(self):

        with open(DB, 'r') as fp:
            lines = fp.readlines()
            with open(DB, 'w') as fp:
                for line in lines:
                    if str(self.name_entry.get()) not in line:
                        fp.write(line)
        self.name_entry.delete(0, 'end')

    def _view(self, head):
        next = Toplevel(head)
        self.view(next)

    def _search(self, head):
        next = Toplevel(head)
        self.search(next)

    def _search_submit(self):
        if len(self.results.get(1.0, 'end')) > 0:
            self.results.delete(1.0, 'end')
        for i in Storage.searchacc:
            if str(self.search_entry.get()) in i[1][0]:
                self.results.insert(END, i[0] + '\n')

    def _update(self, head):
        next = Toplevel(head)
        self.update(next)

    def _update_submit(self):

        with open(DB, 'r') as f:
            # text = ''.join([i for i in f]).replace("pass1", "pass_1")
            texts = [i for i in f]
            for text in texts:
                if str(self.acc_input.get()) in text:
                    new_text = text.replace(str(self.inquire_input.get()), str(self.change_input.get()))
                    texts.append(new_text)
                    texts.remove(text)
            texts = ''.join(texts)

            with open('db.csv', 'w') as fi:
                fi.writelines(texts)

            self.acc_input.delete(0, END)
            self.inquire_input.delete(0, END)
            self.change_input.delete(0, END)

    def _access(self):
        if str(self.password_entry.get()) == f'{PASSWORD}' and str(self.randomized_password.get()) == \
                str(self.random_pass):
            root.destroy()
            next = Tk()
            self.main(next)
        else:
            print("Wrong password!")


if __name__ == "__main__":
    root = Tk()
    program = PaC(root)
    root.geometry('400x190')
    root.resizable(False, False)
    root.title("Accounts and Passwords")
    root.mainloop()
