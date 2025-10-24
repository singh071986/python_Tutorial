import tkinter as tk
from PIL import Image, ImageTk

# Create main window
window = tk.Tk()
window.title("Label & Button Demo")
window.geometry("400x500")

# Label with static text
label_text = tk.Label(window, text='Full name:')
label_text.pack(pady=10)

# Label with textvariable
resultsContents = tk.StringVar()
resultsContents.set('New value to display')
label_var = tk.Label(window, textvariable=resultsContents)
label_var.pack(pady=10)

# Label with resized image
try:
    pil_image = Image.open('/Users/Yuvaan/Downloads/gif.png')
    pil_image = pil_image.resize((200, 200))
    tk_image = ImageTk.PhotoImage(pil_image)
    label_img = tk.Label(window, image=tk_image)
    label_img.image = tk_image
    label_img.pack(pady=10)
except Exception as e:
    label_img_error = tk.Label(window, text='Image not found or unsupported format.', fg='red')
    label_img_error.pack(pady=10)
    tk_image = None  # For button image fallback

# --- Button Features ---
# Callback for button
button_result = tk.StringVar()
def submitForm():
    button_result.set('Button pressed!')

# Basic button
button = tk.Button(window, text='Okay', command=submitForm)
button.pack(pady=10)

# Button with text and image (if image loaded)
if tk_image:
    btn_img = tk.Button(window, text='Image Button', image=tk_image, compound='right', command=lambda: button_result.set('Image Button pressed!'))
    btn_img.image = tk_image
    btn_img.pack(pady=10)

# Default (active) button and Return key binding
active_btn = tk.Button(window, text='Default Action', default='active', command=lambda: button_result.set('Default Action pressed!'))
active_btn.pack(pady=10)
window.bind('<Return>', lambda e: active_btn.invoke())

# Disabled/enabled button demo
state_btn = tk.Button(window, text='Disabled Button', state='disabled')
state_btn.pack(pady=10)

# Show result of button press
result_label = tk.Label(window, textvariable=button_result)
result_label.pack(pady=10)

# --- Entry Features ---
# Basic Entry with textvariable
entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var)
entry.pack(pady=10)

# Button to show current value
entry_result = tk.StringVar()
def show_entry_value():
    entry_result.set(f'Current value is: {entry.get()}')
show_btn = tk.Button(window, text='Show Entry Value', command=show_entry_value)
show_btn.pack(pady=5)

# Button to clear and set value
clear_set_btn = tk.Button(window, text='Clear & Set Value', command=lambda: (entry.delete(0, 'end'), entry.insert(0, 'your name')))
clear_set_btn.pack(pady=5)

# Result label for entry
entry_result_label = tk.Label(window, textvariable=entry_result)
entry_result_label.pack(pady=5)

# Trace changes to entry_var
def entry_changed(*args):
    entry_result.set(f'Entry changed: {entry_var.get()}')
entry_var.trace_add('write', entry_changed)

# Password Entry
password_var = tk.StringVar()
#passwd_entry = tk.Entry(window, textvariable=password_var, show='*')
passwd_entry=tk.Entry(window,textvariable=password_var,show='•') # Using a bullet character for masking
passwd_entry.pack(pady=10)
passwd_label = tk.Label(window, text='Password Entry (hidden):')
passwd_label.pack()

# Button to show password value
show_pass_btn = tk.Button(window, text='Show Password', command=lambda: entry_result.set(f'Password value: {passwd_entry.get()}'))
show_pass_btn.pack(pady=5)

window.mainloop()
