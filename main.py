import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tkinter as tk
from tkinter import ttk
import tkmacosx as tkm
import tkinter.filedialog
from PIL import ImageTk, Image


class HomeScreen(tk.Frame):
	def __init__(self, container):
		super().__init__(container)

		# Define Styles #
		self.style = ttk.Style(self)
		self.style.configure('TLabel', background="white", font=('Roboto', 28))
		self.style.configure('genericText.TLabel', background="white", font=('Roboto', 16))
		self.config(background="white")

		# Sub Container
		self.content_container = tk.Frame(self, background="white")
		ttk.Label(self.content_container, padding=(0, 30), text='Home', style="TLabel").pack()

		# Text
		ttk.Label(self.content_container, wraplength=350, justify="left", padding=(25, 0),
				  text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed  quis sodales erat, vel pellentesque diam. Nulla eu mauris cursus, luctus tellus nec, egestas orci.\n\nFusce consequat, elit tempor dignissim pulvinar, dolor urna sodales augue, eu porttitor tellus orci ac diam. Proin vulputate euismod viverra. Aliquam sit amet pulvinar dui, a volutpat tellus. ',
				  style="genericText.TLabel").pack(side="left")

		# Image
		self.home_image = ImageTk.PhotoImage(Image.open('./assets/home_image.jpg').resize((440, 300)))
		tk.Label(self.content_container, image=self.home_image, width=440, height=300, background="white").pack(
			side='right')
		self.content_container.pack(expand=True)

		self.pack(side='right', expand=True, fill="both")


class AnalysisScreen(tk.Frame):
	def __init__(self, container):
		super().__init__(container)

		def on_configure(event):
			self.canvas.itemconfigure(self.content_container_id, width=event.width)
			self.canvas.configure(scrollregion=self.canvas.bbox('all'))
			self.canvas.yview_moveto(0)

		# Define Styles #
		self.style = ttk.Style(self)
		self.style.configure('TLabel', background="white", font=('Roboto', 28))
		self.style.configure('genericText.TLabel', background="white", font=('Roboto', 16))
		self.config(background="white")

		# Content
		self.canvas = tk.Canvas(self, background="white")
		self.canvas.pack(expand=True, fill="both", side="left")

		self.scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
		self.scrollbar.pack(side="right", fill="y")
		self.canvas.config(yscrollcommand=self.scrollbar.set)

		self.content_container = tk.Frame(self.canvas, bg="white")
		self.canvas.bind('<Configure>', on_configure)
		self.content_container_id = self.canvas.create_window((0, 0), window=self.content_container, anchor='center')

		# Title
		ttk.Label(self.content_container, text='Analysis', style="TLabel").pack()

		# Image
		self.analysis_image = ImageTk.PhotoImage(Image.open('./assets/image_placeholder.jpg').resize((440, 300)))
		self.analysis_image_label = tk.Label(self.content_container, image=self.analysis_image, width=440, height=300,
											 background="white")
		self.analysis_image_label.pack()
		tkm.Button(self.content_container, text="Select image", fg="black",
				   font=tk.font.Font(family='Roboto', size=12), command=self.update_image,
				   background="white", borderless=1, bordercolor="black", activebackground="#2E86AB", padx=5,
				   pady=3).pack()
		ttk.Label(self.content_container, text="1").pack()

		self.pack(side='right', expand=True, fill="both")

	def update_image(self):
		file = tk.filedialog.askopenfilename()
		if file[-3:] != "jpg" and file[-3:] != "png" and file[-4:] != "jpeg":
			tk.messagebox.showinfo(message="File must be an image (PNG, JPG or JPEG).", title="Error")
			return
		self.analysis_image = ImageTk.PhotoImage(Image.open(file).resize((440, 300)))
		self.analysis_image_label.config(image=self.analysis_image)


class HistoryScreen(tk.Frame):
	def __init__(self, container):
		super().__init__(container)

		# Define Styles #
		self.style = ttk.Style(self)
		self.style.configure('TLabel', background="white", font=('Roboto', 28))
		self.style.configure('genericText.TLabel', background="white", font=('Roboto', 16))
		self.config(background="white")

		# Sub Container
		self.content_container = tk.Frame(self, background="white")
		ttk.Label(self.content_container, padding=(0, 30), text='History', style="TLabel").pack()
		self.content_container.pack(expand=True)

		self.pack(side='right', expand=True, fill="both")


class DrawerNavigator(tk.Frame):
	def __init__(self, container):
		super().__init__(container)

		# Sidebar #
		self.sidebar_container = tk.Frame(self, background="#C493B0", padx=50, pady=50)

		# Icon
		self.icon_image = ImageTk.PhotoImage(Image.open('./assets/fertig_logo_purple.png').resize((150, 150)))
		tk.Label(self.sidebar_container, image=self.icon_image, width=150, height=150, background="#C493B0").pack()
		self.sidebar_container.pack(side='left', fill="y")

		# Navigation
		self.navigationOption1 = tk.Frame(self.sidebar_container, pady=20, background="#C493B0")
		self.navigationOption1.pack()
		tkm.Button(self.navigationOption1, command=self.goto_home_screen, fg="black",
				   font=tk.font.Font(family='Roboto', size=16, weight='bold'), text="Home",
				   background="white", borderless=1, bordercolor="black", activebackground="#2E86AB", padx=15,
				   pady=10).pack()
		self.navigationOption2 = tk.Frame(self.sidebar_container, pady=20, background="#C493B0")
		self.navigationOption2.pack()
		tkm.Button(self.navigationOption2, command=self.got_analysis_screen, fg="black",
				   font=tk.font.Font(family='Roboto', size=16, weight='bold'), text="Analysis",
				   background="white", borderless=1, bordercolor="black", activebackground="#2E86AB", padx=15,
				   pady=10).pack()
		self.navigationOption3 = tk.Frame(self.sidebar_container, pady=20, background="#C493B0")
		self.navigationOption3.pack()
		tkm.Button(self.navigationOption3, command=self.goto_history_screen, fg="black",
				   font=tk.font.Font(family='Roboto', size=16, weight='bold'), text="History",
				   background="white", borderless=1, bordercolor="black", activebackground="#2E86AB", padx=15,
				   pady=10).pack()

		# Content #
		self.currentScreen = HomeScreen(self)
		# self.currentScreen = AnalysisScreen(self)

		self.pack(expand=True, fill="both")

	def goto_home_screen(self):
		self.currentScreen.pack_forget()
		self.currentScreen = HomeScreen(self)

	def got_analysis_screen(self):
		self.currentScreen.pack_forget()
		self.currentScreen = AnalysisScreen(self)

	def goto_history_screen(self):
		self.currentScreen.pack_forget()
		self.currentScreen = HistoryScreen(self)


class LandingScreen(tk.Frame):
	def __init__(self, container):
		super().__init__(container)

		# Content Panel #
		self.content_panel = ttk.Frame(self, padding=(0, 55))

		# Background image
		self.background_image = ImageTk.PhotoImage(
			Image.open('./assets/landing_page_background.png').resize((1540, 1080)))
		tk.Label(self.content_panel, image=self.background_image).place(x=0, y=-55)

		# Icon
		self.icon_image = ImageTk.PhotoImage(Image.open('./assets/fertig_logo_squared.png').resize((350, 350)))
		tk.Label(self.content_panel, image=self.icon_image, width=250, height=250, background="white").pack(expand=True,
																											fill="y")
		self.content_panel.pack(expand=True, fill='both')

		# Start button
		tkm.Button(self.content_panel, fg="white", font=tk.font.Font(family='Roboto', size=20, weight='bold'),
				   text="Start", background="#99469E", activebackground="#C493B0", padx=20, pady=15,
				   command=container.goto_drawer_navigator).pack()

		# Footer Panel #
		self.footer_panel = tk.Frame(self)
		tk.Label(self.footer_panel, text='Team Name', font=("Roboto", 16), background="#39A9DB", pady=8).pack(fill='x')
		self.footer_panel.pack(fill='x')

		# heading style
		self.pack(expand=True, fill='both')


class MainNavigator(tk.Frame):
	def __init__(self, container):
		super().__init__(container)

		self.currentScreen = LandingScreen(self)
		# self.currentScreen = DrawerNavigator(self)
		self.pack(expand=True, fill='both')

	def goto_drawer_navigator(self):
		self.currentScreen.pack_forget()
		self.currentScreen = DrawerNavigator(self)


class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title('Fertig App')
		self.geometry('300x50')
		self.minsize(1164, 560)
	# self.state('zoomed')


if __name__ == "__main__":
	app = App()
	MainNavigator(app)
	app.mainloop()
