import os
import openai
import asyncio
from docx import Document
from openpyxl import load_workbook
import pandas as pd
from git import Repo
from base256 import encode as b256_encode, decode as b256_decode

class GPTContentReviewer:
    def __init__(self, model_chat, model_code, model_research, model_recommend):
        self.model_chat = model_chat
        self.model_code = model_code
        self.model_research = model_research
        self.model_recommend = model_recommend

    async def general_chat(self, message):
        encoded_message = b256_encode(message)
        chat_response = await self.gpt_query_with_context(encoded_message, self.model_chat)
        return chat_response

    async def gpt_query_with_context(self, query, model):
        input_encoded = b256_encode(query)
        response = await asyncio.get_event_loop().run_in_executor(None, lambda: openai.Completion.create(engine=model, prompt=input_encoded))
        answer_text = response.choices[0].text.strip()
        return answer_text

    async def process_task(self, task_description):
        encoded_task_description = b256_encode(task_description)

        # 1. docx/xslx review and rewrite.
        file_path_docx_xlsx = "your_docx_or_xlsx_file_here"
        new_file_path_docx_xlsx = await self.process_docx_xlsx_files(file_path_docx_xlsx)

        # 2. local repo coding review and rewrite.
        repo_path = "your_repo_path_here"
        output_path = "your_output_path_here"
        
        await self.process_local_repo(repo_path, output_path)

        # 3. csv processing for eye tracking data assessment.
        eye_tracking_file = "your_eye_tracking_csv_file_here"
        
        review_result = await self.review_eye_tracking_data(eye_tracking_file)

        # 4. general chat with gpt.
        user_message = "Tell me a joke."
        
        chat_response = await self.general_chat(user_message)

        return f"Docx/Xlsx review and rewrite: {new_file_path_docx_xlsx}\nLocal repo coding review and rewrite: Done\nEye tracking data assessment: {review_result}\nGeneral chat: {chat_response}"

    async def process_docx_xlsx_files(self, file_path):
        file_type = os.path.splitext(file_path)[1][1:]

        if file_type == 'docx':
            document = Document(file_path)
            text = '\n'.join([paragraph.text for paragraph in document.paragraphs])
            rewrite_text_question = f"Rewrite the following docx content while retaining its original meaning: {text}"
            rewritten_text = await self.gpt_query_with_context(rewrite_text_question, self.model_chat)

            new_document = Document()
            for paragraph in rewritten_text.split('\n'):
                new_document.add_paragraph(paragraph)

            new_file_path = os.path.splitext(file_path)[0] + '_rewritten.docx'
            new_document.save(new_file_path)

        elif file_type == 'xlsx':
            workbook = load_workbook(file_path)
            sheet = workbook.active
            data = []

            for row in sheet.iter_rows(values_only=True):
                data.append(row)

            df = pd.DataFrame(data[1:], columns=data[0])
            rewrite_xlsx_question = f"Rewrite the following xlsx content while retaining its original meaning: {df.to_csv(index=False)}"
            rewritten_csv_data = await self.gpt_query_with_context(rewrite_xlsx_question, self.model_chat)

            new_df = pd.read_csv(pd.StringIO(rewritten_csv_data))
            new_file_path = os.path.splitext(file_path)[0] + '_rewritten.xlsx'
            new_df.to_excel(new_file_path, index=False)

        return new_file_path

    async def process_local_repo(self, repo_path, output_path):
        repo = Repo(repo_path)
        files = [item.a_path for item in repo.index.diff(None)]

        for file in files:
            if file.endswith(('.docx', '.xlsx', '.csv')):
                file_type = os.path.splitext(file)[1][1:]
                file_path = os.path.join(repo.working_tree_dir, file)

                with open(file_path, 'r') as f:
                    content = f.read()

                task_description = 'your_coding_task_description_here'
                generated_code = await self.review_and_generate_code(content, task_description)

                output_file_name = os.path.splitext(file)[0] + '_generated_code.py'
                output_file_path = os.path.join(output_path, output_file_name)

                with open(output_file_path, 'w') as output_file:
                    output_file.write(generated_code)

                repo.index.add(output_file_path)
                repo.index.commit(f"Add generated code for {file}")

    async def review_and_generate_code(self, content, task_description):
        review_question = f"Review the following content from the file: {content}"
        
        review_result = await self.gpt_query_with_context(review_question, self.model_chat)
        
        question = f"Write code for the following task: {task_description}"
        
        result_encoded = await self.gpt_query_with_context(question, self.model_code)
        
        return result_encoded

    async def review_eye_tracking_data(self, file):
        df = pd.read_csv(file)
        
        review_question = f"Review the following CSV file containing eye-tracking data/floats: {df.to_csv(index=False)}"
        
        review_result = await self.gpt_query_with_context(review_question, self.model_chat)

        return review_result

openai.api_key = 'your_openai_api_key_here'

content_reviewer_app = GPTContentReviewer('gpt-3.5-turbo', 'code-davinci-002', 'text-davinci-002', 'text-davinci-002')

async def main():
    task_description = "Create a script to optimize and synergize everything."
    
    result = await content_reviewer_app.process_task(task_description)
    
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
