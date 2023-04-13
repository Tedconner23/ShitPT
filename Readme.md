# ShitPT, its shit!
# Project: GPT Content Reviewer and Chat Application

This project consists of two Python scripts that work together to create a content review and chat application using OpenAI's GPT-3.5-turbo model. The GPT Content Reviewer script is designed to review content, generate code, and perform various tasks related to content processing. The Chat Application script provides a user interface for users to interact with the GPT Content Reviewer.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Dependencies

- Python 3.7 or higher
- [openai](https://github.com/openai/openai) - OpenAI API client library
- [pandas](https://pandas.pydata.org/) - Data manipulation library
- [docx](https://python-docx.readthedocs.io/en/latest/) - Python library for creating and updating Microsoft Word files
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Python library for reading and writing Excel files
- [GitPython](https://gitpython.readthedocs.io/en/stable/) - Python library for interacting with Git repositories
- [base256](https://pypi.org/project/base256/) - Base256 encoding and decoding library
- [kivy](https://kivy.org/#home) - Python library for building multi-touch applications
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library

## Installation

1. Install Python 3.7 or higher if you haven't already. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone this repository to your local machine:

   ```
   git clone https://github.com/yourusername/yourrepository.git
   ```

3. Navigate to the project directory:

   ```
   cd yourrepository
   ```

4. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # For Linux and macOS
   venv\Scripts\activate  # For Windows
   ```

5. Install the required packages:

   ```
   pip install openai pandas python-docx openpyxl GitPython base256 kivy Pillow
   ```

## Usage

1. Set your OpenAI API key as an environment variable:

   ```
   export OPENAI_API_KEY="your_openai_api_key_here"  # For Linux and macOS
   set OPENAI_API_KEY="your_openai_api_key_here"  # For Windows
   ```

2. Run the Chat Application script:

   ```
   python chat_app.py
   ```

3. Interact with the application by typing messages into the message input field and pressing the send button or the Enter key. The GPT Content Reviewer will process your messages and respond accordingly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
