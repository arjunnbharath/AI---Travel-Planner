# 🧭 Offline AI Travel Planner

An offline travel itinerary generator powered by **LLaMA 3 via Ollama**, built with **Streamlit** and open-source Python libraries.  
Plan your trip with a personalized itinerary, image previews, and export options — all while staying private and offline.

---
## ⚠️ Please Note

> 🕒 **It may run slower** than cloud-based tools — because everything is processed **locally** on your machine.  
> 🧠 The AI is running from a local **LLM (LLaMA 3)** via **Ollama**, so it uses your system’s resources.  
> 🌐 Internet is only used to fetch destination images from Google and to open maps.

**✨ Be patient — your itinerary will be worth it!**

---
## ✨ Features

- 🔐 **Private & Offline**: Works entirely on your computer using a local LLM (LLaMA 3 via Ollama).
- 📍 **Custom AI Travel Itinerary**: Personalized plan based on your destination, trip duration, interests, and budget.
- 🖼️ **5 HD Destination Images**: Fetched directly from Google Images (for educational/demonstration use).
- 📤 **Export Options**: Download your plan as a **PDF** or **TXT** file.
- 💸 **Daily Budget Breakdown**: Automatically calculates a suggested daily spending limit.
- 🗺️ **Google Maps Integration**: Quick link to directions from your location to your destination.

---

## 🚀 Installation & Setup

### 1. 🧠 Install Ollama and Pull LLaMA 3 Model

Ollama lets you run large language models locally.

- **Download Ollama**: https://ollama.com/download  
- **Run the following command to pull the LLaMA 3 model**:

```bash
ollama run llama3
```
### 2. 🐍 Set up Python environment
Clone this repo and install dependencies:
```bash
git clone https://github.com/yourusername/offline-ai-travel-planner
cd offline-ai-travel-planner

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install required packages
pip install -r requirements.txt
```
### 3. 📦 Requirements
Create a requirements.txt file with:
```bash
streamlit
requests
beautifulsoup4
fpdf
Pillow
```
## ▶️Running the App
```bash
streamlit run app.py
```
Then open the link in your browser (usually http://localhost:8501).
## ⚙️ File Structure
```bash
offline-ai-travel-planner/
├── app.py                # Main Streamlit app
├── README.md             # You're here!
└── requirements.txt      # Dependencies
```
## 📥 Export Options
📄 PDF: Nicely formatted, with ₹ replaced by Rs.

📝 TXT: Plain text format for editing

📷 Image Gallery: 5 images fetched from Google in HD (using BeautifulSoup)

## 🔒 Note on Privacy
All processing is done locally:

- No cloud usage

- Your travel data and preferences remain on your machine
## 📌 Known Limitations
- Internet is required only to scrape Google Images.

- The quality of AI output depends on the LLaMA model version used.

- PDF export doesn't embed images (optional future feature).
## 📜 License
- MIT License — free to use, modify, and share.
## 👨‍💻 Author
- Built with ❤️ by [ARJUN BHARATH SR]

- Feel free to fork, extend, or contribute!
```bash

---

Would you like:
- This README as a **downloadable file**?
- A **GIF demo** section added?
- Automatic environment checks (e.g., "is Ollama running?" alerts)?

Let me know and I can add more polish!
