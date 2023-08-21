import os
from flask import Flask, render_template, request, send_file
from gtts import gTTS

app = Flask(__name__, static_folder='static')

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        data = request.form['data']
        output_dir = os.path.join(current_dir, 'media')
        os.makedirs(output_dir, exist_ok=True)  # Create the 'media' directory if it doesn't exist
        output_file = os.path.join(output_dir, 'output.mp3')
        myfile = gTTS(text=data, lang='en', slow=False)
        myfile.save(output_file)
    
    return render_template('download.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        output_file = os.path.join(current_dir, 'media', 'output.mp3')
        return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
