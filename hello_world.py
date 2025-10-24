import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Hello World")
window.geometry("600x400")
window.configure(bg='lightblue')  # Set window background color

# Create and pack first label
Hello = tk.Label(text="Hello, Tkinter")

Hello.pack()

# Create and place second label
Hello2 = tk.Label(window, text="Your First Project")
Hello2.place(x=12, y=50)


# Start the main loop
window.mainloop()