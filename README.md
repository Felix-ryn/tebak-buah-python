# 🍎 Guess the Fruit (Voice-Based Game)

An interactive, educational Python-based game that helps users — especially children — learn to recognize fruits by guessing their names from images **using voice commands**. Built with `Tkinter` for GUI and uses **speech recognition** and **text-to-speech** technologies.

---

## 🔍 Overview

This application displays random fruit images and challenges the user to **guess the fruit name by speaking** into the microphone. It utilizes:

- 🎤 **Speech Recognition** to process spoken input  
- 🗣️ **Text-to-Speech** feedback  
- 🖼️ Random fruit image display  
- ✅ Scoring system and life counter  
- 📦 Packaged in a simple GUI using `Tkinter`  

---

## 🧩 Features

- 🎤 Voice-based guessing using `speech_recognition`
- 🖼️ Random fruit images from local directory
- 🔊 Spoken feedback using `pyttsx3`
- 🧠 Score tracking and 3 lives
- 💻 GUI made with `Tkinter`
- 🇮🇩 Supports Indonesian voice recognition

---

## 🧰 Tech Stack

| Component         | Technology                        |
|-------------------|------------------------------------|
| Programming Lang. | Python 3.x                         |
| GUI               | Tkinter                            |
| Voice Input       | SpeechRecognition + Google API     |
| Voice Output      | pyttsx3 (offline)                  |
| Image Handling    | PIL (Pillow)                       |
| Random Logic      | Python `random`, `os` modules      |

---

## 📂 Project Structure

tebak-buah-python/
├── buah/ # Folder containing fruit images (e.g., apel.jpg)
├── main.py # Main Python application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── ...

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/Felix-ryn/tebak-buah-python.git
cd tebak-buah-python


### 2. Install Dependencies
Create a virtual environment (optional):

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Make sure your microphone is working and connected.

### 3. Run the Application
python main.py

🖼️ Fruit Images Folder
The buah/ folder contains all fruit images used in the game.
Example files:

apel.jpg

pisang.jpg

jeruk.jpg

semangka.jpg

anggur.jpg

These filenames are mapped in the program to their correct Indonesian labels.
You can replace or extend this list by modifying the image_data dictionary inside main.py.

🎮 How to Play
A random fruit image is shown.

Click the “Tebak dengan Suara 🎤” button.

Say the name of the fruit in Indonesian (e.g., “apel”).

If correct → score increases and a new image is shown.

If incorrect → lose a life.

Game ends after 3 wrong guesses.

⚙️ Configuration Notes
speech_recognition uses Google Web Speech API → requires internet connection.

pyttsx3 runs offline to read voice responses.

GUI window size: image is resized to 250x250 pixels.

🧪 Future Improvements
🎥 Add webcam mode for real-time detection

📱 Develop mobile version with Kivy

🧠 Custom vocabulary or dynamic learning mode

🗂️ Image categories by fruit group

🌍 Multi-language support


👨‍💻 Author
Felix Ryan Agusta
GitHub: @Felix-ryn

“Learning through voice and images — for a smarter, more playful generation.” 🎓🍓
