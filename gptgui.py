import os
import openai
import asyncio
import requests
from io import BytesIO
from PIL import Image, ImageTk
from docx import Document
from openpyxl import load_workbook
import pandas as pd
from git import Repo
from base256 import encode as b256_encode, decode as b256_decode
from concurrent.futures import ThreadPoolExecutor
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.text import LabelBase

kivy.require('2.0.0')
# Registering the PixelFont
LabelBase.register(name='PixelFont', fn_regular='path/to/your/VT323-Regular.ttf')

class ImageButton(ButtonBehavior, Image):
    pass
    
    class ImageButton(ButtonBehavior, Image):
        pass


class GPTContentReviewer:
    def __init__(s, model_chat, model_code, model_research, model_recommend):
        s.model_chat = model_chat
        s.model_code = model_code
        s.model_research = model_research
        s.model_recommend = model_recommend
        s.conversation_history = []

    async def gpt_query_with_context(s, question, model):
        role = 'role'
        content = 'content'
        s.conversation_history.append({'role': 'user', 'content': question})
        encoded_conversation_history = [b256_encode(str(msg)) for msg in s.conversation_history]
        response = await openai.ChatCompletion.create(model=model, messages=encoded_conversation_history, max_tokens=1000, n=1, stop=None, temperature=0.7)
        answer = b256_decode(response.choices[0].message[content]).strip()
        s.conversation_history.append({role: 'system', content: answer})
        return answer

    
class Application(ThemedTk):
    def __init__(self):
        super().__init__()
        self.title('ShitPT')
        self.geometry('800x600')
        self.set_theme('equilux')

        self.create_widgets()
        self.set_robot_font()

    def create_widgets(self):
        # Chat history
        self.chat_history = ScrolledText(self, wrap=tk.WORD, font=("Roboto", 12), bg='#1e1e1e', fg='#FFFFFF', state='disabled')
        self.chat_history.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Message input
        self.message_input = ttk.Entry(self, font=("Roboto", 12))
        self.message_input.grid(column=0, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))
        self.message_input.bind('<Return>', self.submit_message)

        # Settings button
        self.settings_button = ttk.Button(self, text='Settings', command=self.open_settings_dialog)
        self.settings_button.grid(column=1, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def open_settings_dialog(self):
        settings_dialog = tk.Toplevel(self)
        settings_dialog.title('Settings')
        settings_dialog.geometry('300x200')

        # Font selection
        font_label = ttk.Label(settings_dialog, text='Select Font:')
        font_label.grid(column=0, row=0, padx=10, pady=10)

        self.font_var = tk.StringVar()
        font_list = ('Roboto', 'Courier', 'Arial', 'Verdana', 'Times New Roman', 'Press Start 2P')
        font_dropdown = ttk.OptionMenu(settings_dialog, self.font_var, *font_list)
        font_dropdown.grid(column=1, row=0, padx=10, pady=10)

        # Save button
        save_button = ttk.Button(settings_dialog, text='Save', command=lambda: self.set_font(self.font_var.get()))
        save_button.grid(column=0, row=1, padx=10, pady=10)

    def set_robot_font(self):
        font_url = 'https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu4mxP.ttf'
        font_path = 'path/to/your/roboto-font.ttf'

        if not os.path.exists(font_path):
            try:
                response = requests.get(font_url)
                with open(font_path, 'wb') as f:
                    f.write(response.content)
            except requests.exceptions.RequestException:
                print("Couldn't load the Roboto font. Check your internet connection.")
                return

        self.robot_font = font_path

    def create_menubar(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        settings_menu = tk.Menu(menubar)
        menubar.add_cascade(label='Settings', menu=settings_menu)

        settings_menu.add_command(label='Fonts', command=self.open_font_dialog)
        settings_menu.add_command(label='Colors', command=self.open_color_dialog)
        settings_menu.add_command(label='API Key', command=self.open_api_key_dialog)
        settings_menu.add_command(label='Folders', command=self.open_folder_dialog)

    def open_font_dialog(self):
        font_dialog = tk.Toplevel(self)
        font_dialog.title('Fonts')
        font_dialog.geometry('300x200')

        # Font selection
        font_list = ('Arial', 'Calibri', 'Courier', 'Helvetica', 'Times New Roman', 'Verdana', 'Roboto')
        font_label = ttk.Label(font_dialog, text='Select Font:')
        font_label.grid(column=0, row=0, padx=10, pady=10)
        font_label = ttk.Label(font_dialog, text='Select Font:')
        font_label.grid(column=0, row=0, padx=10, pady=10)

        self.font_var = tk.StringVar()
        font_dropdown = ttk.OptionMenu(font_dialog, self.font_var, *font_list)
        font_dropdown.grid(column=1, row=0, padx=10, pady=10)

        # Save button
        save_button = ttk.Button(font_dialog, text='Save', command=lambda: self.set_font(self.font_var.get()))
        save_button.grid(column=0, row=1, padx=10, pady=10)

    def open_color_dialog(self):
        color_dialog = tk.Toplevel(self)
        color_dialog.title('Colors')
        color_dialog.geometry('300x200')

        # Color selection
        color_label = ttk.Label(color_dialog, text='Select Text Color:')
        color_label.grid(column=0, row=0, padx=10, pady=10)

        color_button = ttk.Button(color_dialog, text='Choose Color', command=self.choose_color)
        color_button.grid(column=1, row=0, padx=10, pady=10)

    def open_api_key_dialog(self):
        pass  # Implement your API Key setting here

    def open_folder_dialog(self):
        pass  # Implement your folder setting here

    def set_robot_font(self):
        try:
            response = requests.get('https://fonts.gstatic.com/s/roboto/v27/KFOmCnqEu92Fr1Mu72xKKTU1Kg.woff2')
            self.robot_font = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        except requests.exceptions.RequestException:
            print("Couldn't load the Roboto font. Check your internet connection.")
            self.robot_font = None

    def set_font(self, font_name):
        if font_name == 'Roboto' and self.robot_font is not None:
            self.chat_history.config(font=self.robot_font)
        else:
            self.chat_history.config(font=(font_name, 12))

    def choose_color(self):
        color_code = colorchooser.askcolor()[1]
        self.chat_history.config(fg=color_code)

    def submit_message(self, event=None):
        message = self.message_input.get().strip()
        if message:
            self.chat_history.configure(state='normal')
            self.chat_history.insert(tk.END, f'User: {message}\n')
            self.chat_history.configure(state='disabled')
            self.message_input.delete(0, tk.END)

    def set_robot_font(self):
        font_path = 'path/to/your/pixel-font.ttf'
        font_url = 'https://fonts.gstatic.com/s/roboto/v29/KFOmCnqEu92Fr1Mu4mxP.ttf'

        if not os.path.exists(font_path):
            try:
                response = requests.get(font_url)
                with open(font_path, 'wb') as f:
                    f.write(response.content)
            except requests.exceptions.RequestException:
                print("Couldn't load the Roboto font. Check your internet connection.")
                return

        self.robot_font = font_path


class ChatApp(App):
    def build(self):
        self.reviewer_app = GPTContentReviewerApp()
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.chat_history = TextInput(size_hint_y=0.8, readonly=True, multiline=True, font_name='PixelFont', background_color=(1, 1, 0, 1), foreground_color=(0, 0, 0, 1))
        main_layout.add_widget(self.chat_history)
        bottom_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=10)
        self.message_input = TextInput(size_hint_x=0.8, font_name='PixelFont')
        bottom_layout.add_widget(self.message_input)
        send_button = ImageButton(source='path/to/send-button-image.png', size_hint_x=0.2)
        send_button.bind(on_press=self.send_message)
        bottom_layout.add_widget(send_button)
        main_layout.add_widget(bottom_layout)
        self.reviewer = GPTContentReviewer('gpt-3.5-turbo', 'code-davinci-002', 'text-davinci-002', 'text-davinci-002')
        return main_layout

    def send_message(self, instance):
        message = self.message_input.text
        if message:
            self.chat_history.text += f"User: {message}\n"
            self.message_input.text = ''
            response = asyncio.run(self.reviewer_app.general_chat(message))
            self.chat_history.text += f"DIANE: {response}\n"
            animation = Animation(opacity=0.5, duration=0.5) + Animation(opacity=1, duration=0.5)
            animation.start(self.chat_history)

    def update_chat(self, dt):
        self.chat_history.cursor = 0, len(self.chat_history._lines_labels)



if __name__ == '__main__':
    # Downloading the VT323 font if it doesn't exist
    vt323_url = 'https://fonts.gstatic.com/s/vt323/v13/pxiKyp0ihIEF2hsYHpT2dkNE.ttf'
    vt323_path = 'path/to/your/VT323-Regular.ttf'
    if not os.path.exists(vt323_path):
        try:
            response = requests.get(vt323_url)
            with open(vt323_path, 'wb') as f:
                f.write(response.content)
        except requests.exceptions.RequestException:
            print("Couldn't load the VT323 font. Check your internet connection.")
    ChatApp().run()