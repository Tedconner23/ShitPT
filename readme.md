# ShitPT, it's shit!
# GPT Content Reviewer

The GPT Content Reviewer is a powerful and versatile application that integrates OpenAI's GPT-3.5-turbo model to provide various functionalities such as general chat, task processing, file processing, eye-tracking data review, chat-based planning, AI wrangling, and AI rerouting. This application is built using Flask, a lightweight web framework for Python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [General Chat](#general-chat)
  - [Task Processing](#task-processing)
  - [File Processing](#file-processing)
  - [Eye-Tracking Data Review](#eye-tracking-data-review)
  - [Chat-Based Planning](#chat-based-planning)
  - [AI Wrangling](#ai-wrangling)
  - [AI Rerouting](#ai-rerouting)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and run the GPT Content Reviewer, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your_username/gpt-content-reviewer.git
```

2. Navigate to the project directory:

```
cd gpt-content-reviewer
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Set your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY="your_api_key_here"
```

5. Run the application:

```
python app.py
```

The application should now be running on `http://localhost:5000`.

## Usage

### General Chat

The general chat functionality allows users to engage in a conversation with the GPT-3.5-turbo model. Simply type your message into the input field and press "Send" to receive a response from the AI.

### Task Processing

The task processing functionality enables users to provide a task description, and the application will recommend the best approach, research related topics, and generate code to complete the task. The output will be presented in a human-readable format.

### File Processing

The file processing functionality allows users to process `.docx` and `.xlsx` files. The application will rewrite the content of the files while retaining their original meaning. The rewritten files will be saved with a "_rewritten" suffix.

### Eye-Tracking Data Review

The eye-tracking data review functionality enables users to review eye-tracking data stored in a CSV file. The application will provide a review of the data and return the result in a JSON format.

### Chat-Based Planning

The chat-based planning functionality allows users to engage in a conversation with the GPT-3.5-turbo model to plan a specific task or project. Users can continue the conversation until they decide to stop, and the application will provide a summary of the planning session.

### AI Wrangling

The AI wrangling functionality enables users to provide a message, and the application will generate a "wrangled" version of the message using the GPT-3.5-turbo model.

### AI Rerouting

The AI rerouting functionality allows users to provide a message and a target model, and the application will reroute the message to the specified target model, generating a response accordingly.

## API Endpoints

The GPT Content Reviewer provides the following API endpoints:

- `/`: Render the main page of the application.
- `/retro_style.css`: Serve the CSS file for the application.
- `/AI_chat`: Process user input and return a chat response from the GPT-3.5-turbo model.
- `/api/process_folder`: Process a folder containing `.docx` and `.xlsx` files.
- `/api/process_csv`: Process a CSV file containing eye-tracking data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
