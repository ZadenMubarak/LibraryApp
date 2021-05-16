from tkinter import*
from tkinter import messagebox
import sqlite3


conm = sqlite3.connect('book_database.db')
cur = conm.cursor()

conm.execute(""" CREATE TABLE IF NOT EXISTS bookTable (
    book  TEXT  NOT NULL,
    author TEXT  NOT NULL,
    ISBN   TEXT NOT NULL)
""")
root = Tk()
root.title("main window")
root.geometry('460x420')
root.config(bg = 'black')

def done():
        q = messagebox.askyesno('EXIT', 'Are you sure you want to exit?'.title())
        if q == True:
            root.destroy()
        else:
            pass


def search_book():
    for item in root.winfo_children():
        item.destroy()
    button = Button(text='  Add new book   ',fg='yellow',bg='dark green',height=1,width=15,command=saver)
    button.place(x=1, y=30)
    
    root.configure(bg='dark grey')
    root.title('Search Book')
    
    se_text = Label(text='\tSearch Book:\t  ', fg='white', bg='black')
    se_text.pack()
    sh = StringVar()
    search = Entry(textvariable=sh, width=40)
    search.place(x=120, y=130)

    def get_book():
        book = search.get()
        select = cur.execute(f'SELECT * FROM bookTable WHERE book=?', (book,)).fetchall()
        if len(select) == 0:
            messagebox.showinfo('Not found', 'Sorry Book was not found'.title())
        else:
            canvas = Tk()
            canvas.title('Book list')
            canvas.geometry('300x350')
            line = 10
            x_scale = 20
            for i in select:
                author_text = Label(canvas,text=f'Author: {i[1]}')
                author_text.place(x = x_scale, y = line)
                line += 20
                author_text = Label(canvas,text=f'Book: {i[0]}')
                author_text.place(x = x_scale, y = line)
                line += 20
                author_text = Label(canvas,text=f'ISBN: {i[2]}')
                author_text.place(x = x_scale, y = line)
                line += 20
        

    sbut = Button(text = 'search book', fg='silver', bg='teal', height=1, width=10, command=get_book)
    sbut.place(x=120, y=150)
    
    exit_button = Button(text='EXIT!', fg='teal', bg='grey', height=1, width=7, command=done)
    exit_button.place(x=1, y=5)

def saver():
    for item in root.winfo_children():
        item.destroy()
    button2 = Button(text = 'Search Book', fg='gold', bg='brown', height=1, width=10, command=search_book)
    button2.place(x=7, y=30)
    root.title("Add Book")
    root.config(bg = 'teal')
    exit_button = Button(text='EXIT!', fg='teal', bg='grey', height=1, width=7, command=done)
    exit_button.place(x=1, y=8)

    store = StringVar(); etry = Entry(textvariable=store, width=40)
    etry.place(x = 120,y = 130)

    isb_INFO = Label(text=' ISBN: ', fg='black', bg='navy blue')
    isb_INFO.place(x=120, y=155)
    isb = StringVar(); alab = Label(text=' Authors name: ', fg='magenta',bg='dark green')
    alab.place(x=120, y=210)
    ISBN = Entry(textvariable=isb, width=30)
    ISBN.place(x=120, y= 180)
    ainfo = StringVar(); author = Entry(textvariable=ainfo, width=50)
    author.place(x=120, y=230)  

    text = Label(text = '\tAdd Book\t', fg='gold', bg='black')
    text.pack()
    book = Label(text = "    Book name   ", fg='blue', bg='black')
    book.place(x =120, y= 100) 

    
    def save():
            name = store.get(); inum = isb.get(); auname = ainfo.get()
            cur.execute(f"INSERT INTO bookTable VALUES ('{name}', '{auname}', '{isb}')")
            conm.commit()
            ISBN.delete(0, "end")
            etry.delete(0, "end")
            author.delete(0, "end")
            messagebox.showinfo('Saved', 'Book saved'.title())

    button3 = Button(text='  Save!   ',fg='white',bg='navy blue',height=1,width=5,command=save)
    button3.place(x =130, y=230)

if __name__=="__main__":
    button = Button(text='  Add new book   ',fg='yellow',bg='dark green',height=1,width=15,command=saver)
    button.place(x =0, y=0)

    button2 = Button(text = 'Search Book', fg='gold', bg='brown', height=1, width=10, command=search_book)
    button2.place(x =120, y=0)
    root.mainloop()
