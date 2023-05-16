import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from numpy import random

#initialize app
root = tk.Tk()
root.title("My Film List")
root.eval("tk::PlaceWindow . center")

bg_colour = "#3d6466"

def clear_widgets(frame):
	for widget in frame.winfo_children():
		widget.destroy()

def mod_db(entry_id):
	connection = sqlite3.connect("films.db")
	cursor = connection.cursor()
	cursor.execute("select * from films where title = \"" + entry_id + "\"")
	all_tables = cursor.fetchall()
	if all_tables[0][3]:
		cursor.execute("update films set isWatched = False where title = \"" + entry_id+ "\"")
	else:
		cursor.execute("update films set isWatched = True where title = \"" + entry_id+ "\"")

	cursor.execute("update films set isWatched = True where title = entry_id")
	connection.commit()

	#cursor.execute("select * from films where title = \"" + entry_id + "\"")
	#all_tables = cursor.fetchall()
	#print(all_tables)
	#print("signin")	
	connection.close()

def fetch_db():
	connection = sqlite3.connect("films.db")
	cursor = connection.cursor()
	#cursor.execute("SELECT * FROM films where main_genre like '%Fantasy%'")
	cursor.execute("SELECT * from films")
	#cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
	all_tables = cursor.fetchall()
	idx = random.randint(0, len(all_tables)-1)
	print(all_tables[idx])
	table_reg = all_tables[idx]
	connection.close()
	return table_reg

def pre_process(table_name):
	print(table_name)
	title = table_name[1]
	year = table_name[0]
	genres = table_name[2]
	watched = ["Not seen it yet", "Seen it"][table_name[3]]
	print(title, genres)
	return title, year, genres, watched

def load_frame1():
	clear_widgets(frame2)
	frame1.tkraise()
	frame1.pack_propagate(False)
	#logo widget
	image = Image.open('imgs/holo firefox icon.png')
	img = image.resize((350,250))
	logo_img = ImageTk.PhotoImage(img)
	logo_widget = tk.Label(frame1, image=logo_img, bg = "#3d6466")
	logo_widget.image = logo_img
	logo_widget.pack()

	tk.Label(
		frame1,
		text = "ready for la bouche?",
		bg = bg_colour,
		fg = "white",
		font = ("TkMenuFont", 14)
		).pack()

	#button widget
	tk.Button(
		frame1,
		text = "SHUFFLE",
		font=("TkHeadingFont", 20),
		bg="#28393a",
		fg="white",
		cursor="hand2",
		activebackground="#badee2",
		activeforeground="black",
		command=lambda:load_frame2()
		).pack()

def load_frame2():
	clear_widgets(frame1)
	frame2.tkraise()
	print("hellow denise")
	table_reg = fetch_db()
	title, year, genres, watched = pre_process(table_reg)

	
	#logo widget
	image = Image.open('imgs/holo firefox icon.png')
	img = image.resize((350,250))
	logo_img = ImageTk.PhotoImage(img)
	logo_widget = tk.Label(frame2, image=logo_img, bg = "#3d6466")
	logo_widget.image = logo_img
	logo_widget.pack(pady=20)

	tk.Label(
		frame2,
		text = title,
		bg = bg_colour,
		fg = "white",
		font = ("TkHeadingFont", 20)
		).pack(pady=25)
	
	#atributes
	tk.Label(
		frame2,
		text = year,
		bg = bg_colour,
		fg = "white",
		font = ("TkMenuFont", 12)
		).pack()

	tk.Label(
		frame2,
		text = genres,
		bg = bg_colour,
		fg = "white",
		font = ("TkMenduFont", 12)
		).pack()

	tk.Label(
		frame2,
		text = watched,
		bg = bg_colour,
		fg = "white",
		font = ("TkMenduFont", 12)
		).pack()

	#button widget
	tk.Button(
		frame2,
		text = "BACK",
		font=("TkHeadingFont", 18),
		bg="#28393a",
		fg="white",
		cursor="hand2",
		activebackground="#badee2",
		activeforeground="black",
		command=lambda:load_frame1()
		).pack(pady=20)

	tk.Button(
		frame2,
		text = "SET TO VIEWED",
		font=("TkHeadingFont",14),
		bg="#3236a8",
		fg="white",
		cursor="hand2",
		activebackground="#badee2",
		activeforeground="black",
		command=lambda:mod_db(title),
		).pack(pady=20)


frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
	frame.grid(row=0, column=0, sticky="nesw")

load_frame1()
root.wm_attributes('-toolwindow', 'True')
#run app
root.mainloop()