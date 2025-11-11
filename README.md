# 🌸 Henna AI — AI-Powered Mehndi Design Generator

**Henna AI** (also known as *MehndiMuse*) is a smart, AI-powered web app that generates personalized Mehndi (Henna) designs for your hands using **Google Gemini AI** and **Streamlit**.  
It helps you create stunning and realistic henna patterns for **Eid, weddings, parties, or any special occasion** — all in just a few clicks! ✨

---

## 💫 Features

- 🎨 **Multiple Mehndi Styles** – Pakistani, Arabic, Indian, Bridal, Tattoo, and more.
- 🖐️ **Hand Age Selection** – Choose from toddler to senior hands.
- 💍 **Occasion Options** – Eid, Wedding, Festival, Party, or Casual.
- 🧠 **AI-Powered** – Uses Google Gemini for realistic and creative image generation.
- ⚙️ **Complexity Control** – Adjust from simple to intricate patterns.
- ✍️ **Custom Text** – Add your name or message to the Mehndi design.
- 🖼️ **Multiple Outputs** – Generate up to 10 designs at once.
- 🌈 **Beautiful UI** – Modern, festive, and feminine design with inspirational quotes.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Henna-AI.git
cd Henna-AI

### 2️⃣ Set Up Python Environment

Make sure you have Python 3.8+ installed.

Create a virtual environment:

python -m venv venv


Activate it:

# For Windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Add Google Gemini API Key

Create a .env file in the project root and add:

API_KEY=your_gemini_api_key_here


⚠️ Important: Do NOT upload your .env file to GitHub.
(It’s already included in .gitignore to keep your API key private.)

### 5️⃣ Run the App
streamlit run script.py


The app will automatically open in your browser. Enjoy creating your dream henna designs! 🌿

🖼️ Preview

You can add your project screenshot here (optional):

![Henna AI Preview](logo.jpg)

🧠 How It Works

User Input: You choose design type, hand age, occasion, and complexity.

Prompt Generation: App creates a detailed artistic description for the AI.

AI Image Generation: Google Gemini generates realistic hand + mehndi images.

Display: Streamlit beautifully shows all generated designs.

🪷 Customization

Change colors, fonts, and layout inside the CSS section in script.py.

Edit the mehndi_quotes list in script.py to show your favorite quotes.

Replace logo.jpg with your brand/studio logo.

Modify default number of images or styles in the sidebar widgets.

📁 Project Structure
Henna-AI/
│
├── script.py            # Main Streamlit app
├── requirements.txt     # Dependencies list
├── README.md            # Project documentation
├── .gitignore           # Ignored files
├── logo.jpg             # App logo (shown in UI)
└── .env (private)       # Your Gemini API key (not uploaded)

🙏 Acknowledgements

Streamlit

Google Gemini AI

All the artists who make Mehndi a beautiful tradition 💖

