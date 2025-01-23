from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql


# Database
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="hariraja",
    database="library_db"
)
my_database = db_connection.cursor()

# User Interface
class PharmacyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x1080")
        self.root.update()
        self.set_background()
        self.create_labels_and_ui()

    def set_background(self):
        image = Image.open(r"D:\Data Science\tkinter\project\libraray sys\libraray.png")
        image = image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.bg_label = Label(self.root, image=photo)
        self.bg_label.image = photo
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_labels_and_ui(self):
        title_frame = Frame(self.root, bg='#AA8D6F', bd=2)
        title_frame.place(relx=0.04, rely=0.08, relwidth=0.4, anchor="w")

        label = Label(title_frame, fg="white", text="Library Management System", font=("Arial", 24, "bold"), bg='#AA8D6F')
        label.grid(row=0, column=0, padx=80, pady=9)

        frame = Frame(self.root, bg='#AA8D6F', bd=2)
        frame.place(relx=0.04, rely=0.35, relwidth=0.4, anchor="w")

        book_label = Label(frame, fg="white", text="Book Title", font=("Arial", 16, "bold"), bg='#AA8D6F')
        book_label.grid(row=0, column=0, padx=45, pady=10, sticky="w")
        self.book_entry = Entry(frame, font=("Arial", 14), width=20)
        self.book_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        author_label = Label(frame, fg="white", text="Author", font=("Arial", 16, "bold"), bg='#AA8D6F')
        author_label.grid(row=1, column=0, padx=45, pady=10, sticky="w")
        self.author_entry = Entry(frame, font=("Arial", 14), width=20)
        self.author_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        publisher_label = Label(frame, fg="white", text="Publisher", font=("Arial", 16, "bold"), bg='#AA8D6F')
        publisher_label.grid(row=2, column=0, padx=45, pady=10, sticky="w")
        self.publisher_entry = Entry(frame, font=("Arial", 14), width=20)
        self.publisher_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        publication_year_label = Label(frame, fg="white", text="Publication Year", font=("Arial", 16, "bold"), bg='#AA8D6F')
        publication_year_label.grid(row=3, column=0, padx=45, pady=10, sticky="w")
        self.publication_year_entry = Entry(frame, font=("Arial", 14), width=20)
        self.publication_year_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        genre_label = Label(frame, fg="white", text="Genre", font=("Arial", 16, "bold"), bg='#AA8D6F')
        genre_label.grid(row=4, column=0, padx=45, pady=10, sticky="w")
        categories = ["Science Fiction", "Graphic Novel", "Fantasy","Action Adventure","Music", "Literature"]
        self.genre_dropdown = ttk.Combobox(frame, values=categories, font=("Arial", 14))
        self.genre_dropdown.grid(row=4, column=1, padx=20, pady=10, sticky="w")
        self.genre_dropdown.set("Select Genre")

        availability_status_label = Label(frame, fg="white", text="Availability Status", font=("Arial", 16, "bold"), bg='#AA8D6F')
        availability_status_label.grid(row=5, column=0, padx=45, pady=10, sticky="w")
        status_options = ["Available", "Reserved","Checked Out"]
        self.availability_status_dropdown = ttk.Combobox(frame, values=status_options, font=("Arial", 14))
        self.availability_status_dropdown.grid(row=5, column=1, padx=20, pady=10, sticky="w")
        self.availability_status_dropdown.set("Select Status")

        clear = Button(frame, text="Clear All", font=("Arial", 10, "bold"), command=self.clear_fields, bg="gray", fg="black", activebackground="darkgray", activeforeground="white")
        clear.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        add_book_button = Button(self.root, text="Add Book", font=("Arial", 10, "bold"), command=self.add_book, bg="green", fg="white", activebackground="lightgreen", activeforeground="green")
        add_book_button.place(x=115, y=415)

        update_button = Button(self.root, text="Update", font=("Arial", 10, "bold"), command=self.update_record, fg="white", bg="skyblue", activebackground="lightblue", activeforeground="blue")
        update_button.place(x=250, y=415)

        view_button = Button(self.root, text="View All", font=("Arial", 10, "bold"),  fg="white",command=self.view_all_data, bg="violet", activebackground="purple", activeforeground="pink")
        view_button.place(x=470, y=414)

        delete_button = Button(self.root, text="Delete", font=("Arial", 10, "bold"), fg="white", command=self.delete_record, bg="red", activebackground="pink", activeforeground="red")
        delete_button.place(x=590, y=414)

        #style=ttk.Style=()
        #style.configure("MyTreeview",background="#AA8D6F")
        
        
        tree_frame = Frame(self.root)
        tree_frame.place(x=70, y=500, width=600, height=250)

        columns = ("sno", "book Name", "author", "publisher", "publication year", "genre", "Availability Status")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=8)#style="MyTreeview")
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)

        self.tree.heading("sno", text="Sno")
        self.tree.heading("book Name", text="Book Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("publisher", text="Publisher")
        self.tree.heading("publication year", text="Publication Year")

        self.tree.heading("genre", text="Genre")
        self.tree.heading("Availability Status", text="Availability Status")

        self.tree.column("sno", width=20, anchor=CENTER)
        self.tree.column("book Name", width=55, anchor=CENTER)
        self.tree.column("author", width=65, anchor=CENTER)
        self.tree.column("publisher", width=90, anchor=CENTER)
        self.tree.column("publication year", width=45, anchor=CENTER)
        self.tree.column("genre", width=40, anchor=CENTER)
        self.tree.column("Availability Status", width=90, anchor=CENTER)

        scrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

    #Clear Input Fields
    def clear_fields(self):
        self.book_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.publisher_entry.delete(0, END)
        self.publication_year_entry.delete(0, END)
        self.genre_dropdown.set("Select genre")
        self.availability_status_dropdown.set("Select Status")
    #Add Columns
    def add_book(self):
        book_title = self.book_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        publication_year = self.publication_year_entry.get()
        genre = self.genre_dropdown.get()
        availability_status = self.availability_status_dropdown.get()

        if not book_title or not author:
            messagebox.showerror("Error", "Book Name is required.")
            return

        try:
            sql = """INSERT INTO library (book_title, author, publisher, publication_year, genre, availability_status) VALUES (%s, %s, %s, %s, %s, %s)"""
            my_database.execute(sql, (book_title, author, publisher, publication_year, genre, availability_status))
            db_connection.commit()

            self.tree.insert("", "end", values=(len(self.tree.get_children()) + 1,book_title, author, publisher, publication_year, genre, availability_status ))
            self.clear_fields()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to add book: {e}")

    #update the records
    def update_record(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No record selected for update.")
            return
        values = self.tree.item(selected_item, "values")
        if not values:
            return

        sno = values[0]
        book_title = self.book_entry.get()
        author = self.author_entry.get()
        publisher = self.publisher_entry.get()
        publication_year = self.publication_year_entry.get()
        genre = self.genre_dropdown.get()
        availability_status = self.availability_status_dropdown.get()

        try:
            sql = """UPDATE library SET book_title=%s, author=%s,publisher=%s, publication_year=%s, genre=%s, availability_status=%s WHERE book_title=%s"""
            my_database.execute(sql, (book_title, author,publisher, publication_year, genre, availability_status, sno))
            db_connection.commit()

            self.tree.item(selected_item, values=(
                sno, book_title, author,publisher, publication_year, genre, availability_status))
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update record: {e}")

    #delete the records
    def delete_record(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No record selected for deletion.")
            return
        values = self.tree.item(selected_item, "values")
        if not values:
            return
        sno = values[0]

        try:
            sql = "DELETE FROM library WHERE book_title=%s"
            my_database.execute(sql, (sno,))
            db_connection.commit()
            self.tree.delete(selected_item)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete record: {e}")

    #view all records
    def view_all_data(self):
        new_window = Toplevel(self.root)
        new_window.title("book details")
        new_window.geometry("800x400")
        tree_frame = Frame(new_window)
        tree_frame.pack(fill=BOTH, expand=True)
        columns = ("book Name", "author", "publisher", "publication year", "genre", "Availability Status")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        tree.pack(fill=BOTH, expand=True)

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
        try:
            sql = """
                SELECT book_title, author,publisher,publication_year, genre, availability_status
                FROM library
            """
            my_database.execute(sql)
            rows = my_database.fetchall()
            # Insert data into the TreeView
            for row in rows:
                tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {e}")
        
win = Tk()
app = PharmacyApp(win)
win.mainloop()
