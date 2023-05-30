from tkinter import * 
import backend
 
# creating main tkinter window/toplevel
master = Tk()
master.title("GUI SQL display Version 1.0")
master.geometry('425x400') # Set window size

def call():
    command = sql_cmd_entry.get()
    result = backend.sql_conn.execute_sql_command(command)
    sql_cmd_output.insert(1.0, result)
    
def delete():
    sql_cmd_output.delete(1.0, END)

# START wigets
sql_cmd_label = Label(master, text="Enter your SQL command:")
sql_cmd_entry = Entry(master)

sql_cmd_button = Button(master, text="Enter SQL", command=call, padx=10)
sql_cmd_button_delete = Button(master, text="Delete output", command=delete, padx=10)

header_output = Label(master, pady=10, text = "Output: ", font=("Comic Sans MS", 20))
sql_cmd_output = Text(master, width=50, height=10)
# END wigets

# START Place Wigets

sql_cmd_label.grid(row = 1, column = 1, padx=20, pady=10)
sql_cmd_entry.grid(row = 2, column = 1, pady=10,)
sql_cmd_button.grid(row = 3, column = 1,)
sql_cmd_button_delete.grid(row = 4, column = 1, pady=10)
header_output.grid(row = 5, column = 1)
sql_cmd_output.grid(row = 6, column = 1, padx=10)


# START Place Wigets

mainloop()