# ShitPT, its shit!
# GPT Content Reviewer

The GPT Content Reviewer is a Python script that utilizes OpenAI's GPT-3.5-turbo and code-davinci-002 models to help you plan, consolidate context, and execute coding tasks. It fetches the context from a Git repository and passes it to the coders to generate the required code.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- openai Python package
- python-docx package
- openpyxl package
- pandas package
- GitPython package
- base256 package

You can install the required packages using pip:

```bash
pip install openai python-docx openpyxl pandas GitPython base256
```

### Usage

1. Set your OpenAI API key in the script:

```python
openai.api_key = 'your_openai_api_key_here'
```

2. Customize the `local_repo_directory`, `planning_question`, and `task_description` variables in the `main()` function:

```python
local_repo_directory = '/path/to/your/local/repository'
planning_question = "your_planning_question_here"
task_description = "your_coding_task_description_here"
```

3. Run the script:

```bash
python gpt_content_reviewer.py
```

The script will perform the following steps:

1. Plan with GPT: Send your planning question to GPT-3.5-turbo and receive a planning result.
2. Consolidate context from the repository: Fetch the context from the local Git repository and consolidate it.
3. Execute the coding task with the context: Send the task description and context to code-davinci-002 to generate the required code.

The generated code will be printed on the console.

## License

This project is licensed under the MIT License.

## Acknowledgments

- OpenAI for providing the GPT-3.5-turbo and code-davinci-002 models
```

This README.md file provides an overview of the GPT Content Reviewer script, the prerequisites, usage instructions, and acknowledgments. You can include this file in your project's repository to help others understand and use the script. 😊