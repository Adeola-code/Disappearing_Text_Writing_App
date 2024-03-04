import tkinter as tk

class DisappearingTextWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adeola's Disappearing Text Writing App")
        self.timeout_seconds = 10
        self.text = ""

        self.text_entry = tk.Text(root, wrap="word", height=10, width=40)
        self.text_entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Writing", command=self.start_writing)
        self.start_button.pack(pady=10)

        self.countdown_label = tk.Label(root, text=f"Time remaining: {self.timeout_seconds} seconds")
        self.countdown_label.pack()

        self.timeout_id = None

    def start_writing(self):
        self.text_entry.delete("1.0", tk.END)
        self.text = ""
        self.timeout_seconds = 10
        self.start_button.config(state=tk.DISABLED)
        self.root.bind("<Key>", self.on_key_press)
        self.countdown()

    def on_key_press(self, event):
        self.text += event.char
        self.reset_countdown()

    def countdown(self):
        if self.timeout_seconds > 0:
            self.countdown_label.config(text=f"Time remaining: {self.timeout_seconds} seconds")
            self.timeout_seconds -= 1
            self.timeout_id = self.root.after(1000, self.countdown)
        else:
            self.clear_text()

    def reset_countdown(self):
        if self.timeout_id:
            self.root.after_cancel(self.timeout_id)
        self.timeout_seconds = 10
        self.countdown()

    def clear_text(self):
        self.root.unbind("<Key>")
        self.text_entry.delete("1.0", tk.END)
        self.text = ""
        self.start_button.config(state=tk.NORMAL)
        self.countdown_label.config(text="Time's up! Progress has been lost.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextWritingApp(root)
    app.run()
