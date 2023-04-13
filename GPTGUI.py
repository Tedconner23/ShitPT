import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import asyncio
from gptpy import GPTContentReviewer

class GPTContentReviewerGUI(tk.Tk):
    def __init__(self, content_reviewer_app):
        super().__init__()
        self.title('GPT Content Reviewer')
        self.geometry('1280x730')
        self.content_reviewer = content_reviewer_app
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self, text='Input:', font=('Arial', 16))
        self.input_label.grid(row=0, column=0, padx=20, pady=20, sticky='W')

        self.input_text = tk.Text(self, wrap='word', height=12, width=80, font=('Arial', 14))
        self.input_text.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.process_button = tk.Button(self, text='Process', font=('Arial', 16), command=self.process_input)
        self.process_button.grid(row=2, column=0, padx=20, pady=20)

        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=200, mode='indeterminate')
        self.progress_bar.grid(row=2, column=1, padx=20, pady=20)

        self.output_label = tk.Label(self, text='Output:', font=('Arial', 16))
        self.output_label.grid(row=3, column=0, padx=20, pady=20)

        self.output_text = tk.Text(self, wrap='word', height=20, width=80, font=('Arial', 14))
        self.output_text.config(state='disabled')
        self.output_text.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

    async def process_and_display_output(self):
        self.progress_bar.start()
        user_input = self.input_text.get('1.0', tk.END).strip()

        if not user_input:
            messagebox.showwarning('Empty Input', 'Please enter some text before processing.')
            self.progress_bar.stop()
            return

        result = await self.content_reviewer.general_chat(user_input)
        self.progress_bar.stop()
        self.display_output(result)

    def process_input(self):
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.config(state='disabled')
        asyncio.create_task(self.process_and_display_output())

    def display_output(self, output):
        self.output_text.config(state='normal')
        self.output_text.insert('1.0', output)
        self.output_text.config(state='disabled')

if __name__ == '__main__':
    app = GPTContentReviewer('gpt-3.5-turbo', 'code-davinci-002', 'text-davinci-002', 'text-davinci-002')
    gui = GPTContentReviewerGUI(app)
    gui.mainloop()
