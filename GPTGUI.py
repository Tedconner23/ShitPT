import tkinter as tk
from tkinter import ttk, scrolledtext
from main_script import GPTContentReviewer

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GPT Content Reviewer")
        self.geometry("600x500")
        self.configure(bg="#f0f0f0")

        self.model_review = "gpt-3.5-turbo"
        self.model_code = "code-davinci-002"
        self.reviewer = GPTContentReviewer(self.model_review, self.model_code)

        self.create_widgets()

    def create_widgets(self):
        chat_frame = ttk.Frame(self)
        chat_frame.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        chat_frame.configure(bg="#f0f0f0")

        self.chat_history = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state='disabled', width=50, height=15, bg="#ffffff", fg="#000000", font=("Arial", 12))
        self.chat_history.grid(column=0, row=0, padx=10, pady=10)
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, "Welcome to GPT Content Reviewer!\n\n")
        self.chat_history.configure(state='disabled')

        input_frame = ttk.Frame(self)
        input_frame.grid(column=0, row=1, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        input_frame.configure(bg="#f0f0f0")

        self.message_input = ttk.Entry(input_frame, width=40, font=("Arial", 12))
        self.message_input.grid(column=0, row=0, padx=10, pady=10)
        self.message_input.bind('<Return>', self.submit_message)

        submit_button = ttk.Button(input_frame, text="Submit", command=self.submit_message, style="Submit.TButton")
        submit_button.grid(column=1, row=0, padx=10, pady=10)

        self.style = ttk.Style()
        self.style.configure("Submit.TButton", font=("Arial", 12))

    def submit_message(self, event=None):
        message = self.message_input.get()
        if message:
            self.chat_history.configure(state='normal')
            self.chat_history.insert(tk.END, f'You: {message}\n')
            self.chat_history.configure(state='disabled')

            response = self.reviewer.general_chat(message)
            self.chat_history.configure(state='normal')
            self.chat_history.insert(tk.END, f'DIANE: {response}\n')
            self.chat_history.configure(state='disabled')

            self.chat_history.yview(tk.END)
            self.message_input.delete(0, tk.END)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
