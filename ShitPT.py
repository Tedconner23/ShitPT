from flask import Flask, render_template, request, jsonify
from GPT import GPTContentReviewer, FlaskDataOverride
from flask import send_from_directory

app = Flask(__name__, static_folder='static')
content_reviewer_app = GPTContentReviewer('gpt-3.5-turbo', 'code-davinci-002', 'text-davinci-002', 'text-davinci-002')
flask_data_override = FlaskDataOverride(app)

@app.route('/')
def index():
    return render_template('ShitPT.html')

@app.route('/retro_style.css')
def serve_css():
    return send_from_directory('static', 'retro_style.css')

@app.route('/AI_chat', methods=['POST'])
def ai_chat():
    try:
        data = request.get_json()
        user_input = data.get('message')
        if user_input is None:
            raise KeyError("message key not found in request data")
        print(f"Request: {request}")
        print(f"User input: {user_input}")
        chat_response = content_reviewer_app.general_chat(user_input)
        return jsonify(chat_response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/process_folder', methods=['POST'])
def process_folder():
    folder_path = request.form['folder_path']
    flask_data_override.override_folder(folder_path)
    flask_data_override.update_content_reviewer_app()
    content_reviewer_app.process_files_in_folder(folder_path)
    return jsonify("Folder processed successfully.")

@app.route('/api/process_csv', methods=['POST'])
def process_csv():
    csv_path = request.form['csv_path']
    api_key = request.form['api_key']
    flask_data_override.override_key(api_key)
    flask_data_override.update_content_reviewer_app()
    review_result = content_reviewer_app.review_eye_tracking_data(csv_path)
    return jsonify(review_result)


if __name__ == '__main__':
    app.run(debug=True)
