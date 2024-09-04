from flask import Blueprint, request, render_template
from openai import OpenAI

client = OpenAI(api_key='API_KEY_OPENAI')

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/generate', methods=['POST'])
def generate():
    input_text = request.form.get('input_text')
    if not input_text:
        return "No input text provided", 400
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": input_text}]
        )
        generated_text = response.choices[0].message.content.strip()
        return render_template('result.html', result=generated_text)
    except Exception as e:
        return f"An error occurred: {e}", 500
