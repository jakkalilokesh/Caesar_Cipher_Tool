# Caesar Cipher - Secure Text Encryption Tool

A professional web application for encrypting and decrypting text using the classic *Caesar cipher algorithm*.  
Built with a *Python Flask backend* and a responsive *HTML/CSS frontend*.

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)

---

## Features

-  *Secure Encryption/Decryption* – Uses the historic Caesar cipher algorithm  
-  *Real-time Processing* – Instant text transformation  
-  *Fully Responsive* – Works perfectly on all devices  
-  *Professional UI* – Clean, modern interface with light theme  
-  *Easy to Use* – Intuitive controls and clear instructions  
-  *Live Statistics* – Character and word counts  
-  *Privacy Focused* – No data storage (all processing happens in memory) 

---

## Quick Start

### Prerequisites
- Python *3.7+*
- *pip* (Python package manager)

### Installation

1. *Clone the repository*
   bash
   git clone https://github.com/yourusername/caesar-cipher.git
   cd caesar-cipher
   

2. *Create a virtual environment (recommended)*
   bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. *Install dependencies*
   bash
   pip install flask
   

4. *Run the application*
   bash
   python app.py
   

5. *Open your browser*  
   Navigate to 👉 [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

caesar-cipher/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   └── style.css          # CSS stylesheets
└── README.md              # Project documentation


---

## 🛠 How to Use

### Encryption
1. Select *"Encrypt"* mode using the toggle buttons  
2. Enter your *plain text* in the input area  
3. Set the *shift value (1–25)* using the number input  
4. Click *"Encrypt Text"*  
5. Get your *encrypted text* in the output area  

### Decryption
1. Select *"Decrypt"* mode  
2. Paste the *encrypted text*  
3. Set the *same shift value* used during encryption  
4. Click *"Decrypt Text"*  
5. Retrieve your *original text*  

### Additional Features
- *Clear Input:* Clear only the input text field  
- *Clear Output:* Clear only the output text field  
- *Clear All:* Clear both fields  
- *Live Character Count:* Real-time character statistics  
- *Shift Example:* Visual example showing how letters transform  

---

## 🔧 Technical Details

### Caesar Cipher Algorithm
The *Caesar cipher* is one of the simplest and most widely known encryption techniques.  
It’s a *substitution cipher* where each letter in the plaintext is shifted a fixed number of positions down the alphabet.

*Example (shift = 3):*

A → D
B → E
...
X → A
Y → B
Z → C


### Technologies Used
- *Backend:* Python Flask  
- *Frontend:* HTML5, CSS3  
- *Icons:* Font Awesome  
- *Fonts:* Google Fonts (Inter)  
- *Styling:* Pure CSS (no JavaScript)  

---

## Security Notes
- This project is for *educational purposes only*  
- Caesar cipher is *not secure* for modern cryptographic use  
- All processing happens *in memory* (no data stored)  
- Intended for *learning and demonstration*

---

## Use Cases
- Learning about *cryptography basics*  
- Simple *text obfuscation*  
- *Programming demonstrations*  
- *Historical algorithm* exploration  

---

## Customization
You can easily modify the application by:

- *Changing the theme:* Edit colors in static/style.css  
- *Adding features:* Extend logic in app.py  
- *Modifying UI:* Update templates/index.html

---

## Troubleshooting

| Issue | Solution |
|-------|-----------|
| *Port already in use* | Use another port → python app.py --port 5001 |
| *Flask not found* | Reinstall Flask → pip install --force-reinstall flask |
| *CSS not loading* | Check static file structure & clear browser cache |
