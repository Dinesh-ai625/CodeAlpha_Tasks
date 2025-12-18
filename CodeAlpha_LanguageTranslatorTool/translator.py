from tkinter import *
from tkinter import font
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():
    input_text = text_input.get("1.0", END)
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()

    if input_text.strip() == "":
        text_output.delete("1.0", END)
        text_output.insert(END, "Please enter text to translate.")
        return

    result = GoogleTranslator(source=src_lang, target=dest_lang).translate(input_text)
    text_output.delete("1.0", END)
    text_output.insert(END, result)

# Main window
root = Tk()
root.title("Language Translator")
root.geometry("820x620")
root.config(bg="#004d40")  # Vibrant emerald black green

# Fonts
title_font = font.Font(family="Helvetica", size=28, weight="bold")
label_font = font.Font(family="Helvetica", size=14, weight="bold")
text_font = font.Font(family="Helvetica", size=12, weight="bold")
button_font = font.Font(family="Helvetica", size=14, weight="bold")
dropdown_font = font.Font(family="Helvetica", size=12, weight="bold")

# Title
Label(root, text="Language Translator", font=title_font, bg="#004d40", fg="#FFFFFF").pack(pady=15)

# Input text box
Label(root, text="Enter Text:", font=label_font, bg="#00796b", fg="#FFFFFF", padx=5, pady=5).pack(pady=(5,0))
text_input = Text(root, height=8, width=90, font=text_font, bg="#00796b", fg="#FFFFFF", insertbackground="white")
text_input.pack(pady=5)

# Language options frame (From & To side by side)
lang_frame = Frame(root, bg="#004d40")
lang_frame.pack(pady=10)

languages = ["auto", "en", "hi", "fr", "es", "de", "it", "zh", "ar", "ru"]

src_lang_var = StringVar(root)
src_lang_var.set("auto")
dest_lang_var = StringVar(root)
dest_lang_var.set("en")

# From dropdown
Label(lang_frame, text="From:", font=label_font, bg="#004d40", fg="#FFFFFF").grid(row=0, column=0, padx=10)
from_menu = OptionMenu(lang_frame, src_lang_var, *languages)
from_menu.config(font=dropdown_font, bg="#00695c", fg="#FFFFFF", width=8, height=1, relief="flat", highlightthickness=0)
from_menu.grid(row=0, column=1, padx=10)

# To dropdown
Label(lang_frame, text="To:", font=label_font, bg="#004d40", fg="#FFFFFF").grid(row=0, column=2, padx=10)
to_menu = OptionMenu(lang_frame, dest_lang_var, *languages)
to_menu.config(font=dropdown_font, bg="#00695c", fg="#FFFFFF", width=8, height=1, relief="flat", highlightthickness=0)
to_menu.grid(row=0, column=3, padx=10)

# Output text box
Label(root, text="Translated Text:", font=label_font, bg="#00796b", fg="#FFFFFF", padx=5, pady=5).pack(pady=(10,0))
text_output = Text(root, height=8, width=90, font=text_font, bg="#00796b", fg="#FFFFFF", insertbackground="white")
text_output.pack(pady=5)

# Translate button below output box, slightly bigger, new color, closer
Button(root, text="Translate", command=translate_text, font=button_font, bg="#388e3c", fg="#FFFFFF", padx=25, pady=12).pack(pady=10)

root.mainloop()
