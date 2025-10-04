from flask import Flask, request, render_template

app = Flask(__name__)

def caesar_cipher(text, shift, operation):
    if not text:
        return ""
    
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if operation == 'encrypt':
                shifted = (ord(char) - ascii_offset + shift) % 26
            else:
                shifted = (ord(char) - ascii_offset - shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ""
    output_text = ""
    shift = 3
    mode = "encrypt"
    alert_message = ""
    alert_type = ""
    
    if request.method == 'POST':
        mode = request.form.get('mode', 'encrypt')
        
        try:
            shift = int(request.form.get('shift', 3))
            if shift < 1 or shift > 25:
                shift = 3
                alert_message = "Shift must be between 1-25. Reset to 3."
                alert_type = "warning"
        except:
            shift = 3
            alert_message = "Invalid shift value. Reset to 3."
            alert_type = "warning"
        
        input_text = request.form.get('input_text', '')
        
        if 'process' in request.form:
            if input_text.strip():
                output_text = caesar_cipher(input_text, shift, mode)
                alert_message = f"Text successfully {mode}ed!"
                alert_type = "success"
            else:
                alert_message = "Please enter some text to process!"
                alert_type = "error"
        
        elif 'clear_input' in request.form:
            input_text = ""
            alert_message = "Input cleared!"
            alert_type = "info"
        
        elif 'clear_output' in request.form:
            output_text = ""
            alert_message = "Output cleared!"
            alert_type = "info"
        
        elif 'clear_all' in request.form:
            input_text = ""
            output_text = ""
            alert_message = "All fields cleared!"
            alert_type = "info"
    
    return render_template('index.html', 
                         input_text=input_text,
                         output_text=output_text,
                         shift=shift,
                         mode=mode,
                         alert_message=alert_message,
                         alert_type=alert_type)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)