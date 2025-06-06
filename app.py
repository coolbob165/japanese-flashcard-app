import tkinter as tk
import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

flashcards = [
    {"kana": "こんにちは", "romaji": "konnichiwa", "english": "Hello"},
    {"kana": "ありがとう", "romaji": "arigatou", "english": "Thank you"},
    {"kana": "さようなら", "romaji": "sayounara", "english": "Goodbye"},
    {"kana": "おはよう", "romaji": "ohayou", "english": "Good morning"},
    {"kana": "こんばんは", "romaji": "konbanwa", "english": "Good evening"},
]

class JapaneseFlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌙 Quick Japanese Learner - Dark Mode")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e1e")

        self.showing_answer = False

        self.label = tk.Label(root, text="", font=("Helvetica", 32),
                              bg="#1e1e1e", fg="#ffffff", wraplength=450)
        self.label.pack(pady=60)

        self.flip_button = tk.Button(root, text="Show Answer",
                                     font=("Helvetica", 16),
                                     command=self.flip_card,
                                     bg="#333333", fg="#00ffcc", activebackground="#444444")
        self.flip_button.pack(pady=20)

        self.speak_button = tk.Button(root, text="🔊 Hear it",
                                      font=("Helvetica", 14),
                                      command=self.speak_kana,
                                      bg="#222222", fg="#66ff99", activebackground="#444444")
        self.speak_button.pack(pady=10)

        self.next_card()

    def next_card(self):
        self.current = random.choice(flashcards)
        self.label.config(text=self.current["kana"])
        self.showing_answer = False
        self.flip_button.config(text="Show Answer")

    def flip_card(self):
        if self.showing_answer:
            self.next_card()
        else:
            self.label.config(
                text=f"{self.current['romaji']} - {self.current['english']}")
            self.flip_button.config(text="Next")
            self.showing_answer = True

    def speak_kana(self):
        engine.say(self.current["kana"])
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = JapaneseFlashcardApp(root)
    root.mainloop()
