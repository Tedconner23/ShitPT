# ShitPT, its shit!
# Project Title: GPT Content Reviewer and Chat Application

This project combines the power of OpenAI's GPT-3.5-turbo model with a user-friendly chat interface to create a versatile content reviewer and chat application. The application can review and generate code, rewrite documents, process local repositories, and much more.

## Features

- Review and generate code from task descriptions
- Process local Git repositories, generating code for specific files
- Rewrite `.docx`, `.xlsx`, and `.csv` files, retaining their original meaning
- Perform research on given topics
- Recommend best approaches for problem-solving
- Chat-based planning with GPT-3.5-turbo
- AI wrangling and rerouting of user messages
- Customizable chat interface with various font and color options

## Getting Started

To get started with the GPT Content Reviewer and Chat Application, follow these steps:

1. Clone the repository or download the source code.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Replace the placeholder API key in the source code with your own OpenAI API key.
4. Run the `main.py` script to launch the application.

## Usage

The chat interface allows you to communicate with the GPT-3.5-turbo model directly. Type your message in the input field and press Enter or click the Send button to submit your message. The model's response will appear in the chat history.

To review and generate code, process local repositories, rewrite documents, or perform research, use the provided functions in the `GPTContentReviewer` class. You can customize these functions and integrate them into your own applications as needed.

## Customization

The chat interface can be customized with different fonts and colors. To change the font, open the Settings dialog and select your desired font from the dropdown menu. To change the text color, open the Colors dialog and choose a color using the color picker.

## Dependencies

- Python 3.7+
- OpenAI
- Pandas
- Openpyxl
- Python-docx
- GitPython
- Base256
- Kivy

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
