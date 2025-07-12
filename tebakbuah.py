import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import speech_recognition as sr
import pyttsx3

# === SETUP ===
image_folder = "buah"
image_data = {
    "apel.jpg": "apel",
    "jeruk.jpg": "jeruk",
    "pisang.jpg": "pisang",
    "semangka.jpg": "semangka",
    "anggur.jpg": "anggur"
}
image_files = list(image_data.keys())
current_answer = ""
score = 0
lives = 3

# === Text-to-Speech Engine ===
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # kecepatan bicara

def speak(text):
    engine.say(text)
    engine.runAndWait()

def show_new_image():
    global current_answer, img_display

    filename = random.choice(image_files)
    current_answer = image_data[filename].lower()

    img_path = os.path.join(image_folder, filename)
    img = Image.open(img_path)
    img = img.resize((250, 250), Image.Resampling.LANCZOS)
    img_display = ImageTk.PhotoImage(img)

    canvas.image = img_display
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=img_display)

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Rekam", "Silakan sebut nama buah...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="id-ID")
            print("Kamu bilang:", text)
            check_answer(text)
        except sr.UnknownValueError:
            messagebox.showerror("Gagal", "Suara tidak dikenali.")
            speak("Suara tidak dikenali.")
        except sr.RequestError:
            messagebox.showerror("Error", "Tidak bisa mengakses layanan Google.")
            speak("Gagal mengakses Google Speech.")

def check_answer(user_answer):
    global score, lives

    user_answer = user_answer.strip().lower()
    if user_answer == current_answer:
        score += 1
        update_status()
        speak("Benar!")
        messagebox.showinfo("Benar!", f"Jawaban benar: {current_answer}")
        show_new_image()
    else:
        lives -= 1
        update_status()
        speak(f"Salah. Jawabannya {current_answer}")
        if lives == 0:
            messagebox.showerror("Game Over", f"Kamu kehabisan nyawa!\nSkor akhir: {score}")
            speak(f"Game over. Skormu {score}")
            root.destroy()
        else:
            messagebox.showerror("Salah", f"Kamu bilang '{user_answer}', bukan {current_answer}")

def update_status():
    score_label.config(text=f"Skor: {score}")
    lives_label.config(text=f"Nyawa: {lives}")

# === GUI ===
root = tk.Tk()
root.title("Tebak Gambar Buah (Suara)")

canvas = tk.Canvas(root, width=250, height=250)
canvas.pack(pady=10)

voice_button = tk.Button(root, text="Tebak dengan Suara 🎤", command=recognize_voice)
voice_button.pack(pady=10)

status_frame = tk.Frame(root)
status_frame.pack(pady=5)
score_label = tk.Label(status_frame, text=f"Skor: {score}", font=("Arial", 12))
score_label.pack(side="left", padx=10)
lives_label = tk.Label(status_frame, text=f"Nyawa: {lives}", font=("Arial", 12))
lives_label.pack(side="left", padx=10)

show_new_image()
root.mainloop()
