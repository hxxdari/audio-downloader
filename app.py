
from flask import Flask, render_template, request, send_file
from downloader import download_audio
import openai
import os

openai.api_key = "sk-..."  # 👈 کلید OpenAI خودت رو اینجا بذار

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gpt_response = ""
    if request.method == "POST":
        if "url" in request.form:
            url = request.form.get("url")
            format_choice = request.form.get("format")
            file_path = download_audio(url, format_choice)
            if file_path:
                return send_file(file_path, as_attachment=True)
            else:
                return "خطا در پردازش لینک!"
        elif "message" in request.form:
            user_message = request.form.get("message")
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_message}]
                )
                gpt_response = response.choices[0].message['content']
            except Exception as e:
                gpt_response = "خطا در پاسخ: " + str(e)

    return render_template("index.html", gpt_response=gpt_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
