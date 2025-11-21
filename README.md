# LLM Question & Answer System

A simple CLI and Web GUI application for asking questions to Google Gemini AI.

## 📋 Project Structure

```
LLM_QA_Project_israel_123456/
├── LLM_QA_CLI.py                    # Command-line interface
├── app.py                           # Flask web application
├── requirements.txt                 # Python dependencies
├── templates/
│   └── index.html                  # Web UI template
├── static/
│   └── style.css                   # Web UI styling
├── LLM_QA_hosted_webGUI_link.txt   # Deployment info
├── README.md                       # This file
└── .gitignore                      # Git ignore rules
```

## 🔑 Getting Your Gemini API Key

### Step 1: Get API Key from Google AI Studio
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **"Get API Key"** in the top navigation
3. Sign in with your Google account
4. Click **"Create API Key"**
5. Select **"Create API key in new project"** (recommended)
6. Copy the generated API key (starts with `AIza...`)

### Step 2: Set Environment Variable
```bash
# On macOS/Linux (add to ~/.zshrc or ~/.bashrc for persistence)
export GEMINI_API_KEY="AIzaSyCHf8LoLJCEu186BcJwoppruA--LpN8KBI"

# On Windows (Command Prompt)
set GEMINI_API_KEY=AIzaSyCHf8LoLJCEu186BcJwoppruA--LpN8KBI

# On Windows (PowerShell)
$env:GEMINI_API_KEY="AIzaSyCHf8LoLJCEu186BcJwoppruA--LpN8KBI"
```

### Step 3: Benefits of Gemini
- **Free Tier**: Generous free quota (15 requests per minute)
- **No Credit Card**: No payment required for basic usage
- **Fast & Reliable**: Google's latest AI technology
- **Easy Setup**: Simple API key creation

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### 2. Set Your API Key

```bash
export GEMINI_API_KEY="AIzaSyCHf8LoLJCEu186BcJwoppruA--LpN8KBI"
```

### 3. Run the CLI

```bash
# Interactive mode
python LLM_QA_CLI.py

# One-shot mode
python LLM_QA_CLI.py "What is machine learning?"
```

### 4. Run the Web GUI

```bash
python app.py
```

Then open your browser to [http://localhost:5000](http://localhost:5000)

## 🌐 Deployment Options

### Option A: Heroku (Recommended)

**Quick Deploy Button:**
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Oluiy/LLM_QA_Project_AKINBOYEWA_23CG034029-)

**Manual Setup:**
1. Push your code to GitHub ✅ **DONE**
2. Create account at [heroku.com](https://heroku.com)
3. Create new app: `heroku create llm-qa-akinboyewa-23cg034029`
4. Set environment variable: `heroku config:set GEMINI_API_KEY=AIzaSyCHf8LoLJCEu186BcJwoppruA--LpN8KBI`
5. Deploy: `git push heroku main`
6. Open: `heroku open`

### Option B: Render.com
1. Create account at [render.com](https://render.com)
2. Create new "Web Service" → Connect GitHub repo
3. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variable**: `GEMINI_API_KEY` = AIzaSyCHf8LoLJCEu186BcJwoppruA--LpN8KBI
4. Deploy and copy the live URL

### Option C: Railway
1. Create account at [railway.app](https://railway.app)
2. Connect GitHub repo
3. Add environment variable: `GEMINI_API_KEY`
4. Deploy automatically

## 🔧 Features

### CLI Application (`LLM_QA_CLI.py`)
- Accepts questions via command line or interactive input
- Preprocesses text (lowercasing, tokenization, punctuation removal)
- Sends formatted prompts to Claude API
- Displays processed tokens and final answer
- Graceful fallback when API key is missing

### Web GUI (`app.py`)
- Clean HTML form for entering questions
- Shows processed question tokens
- Displays Claude's response
- Responsive design with simple CSS
- Error handling for API issues

## 📝 Development Notes

- **Model Used**: Gemini 1.5 Flash (fast and free)
- **Preprocessing**: Converts to lowercase, removes punctuation, tokenizes on whitespace
- **Error Handling**: Both apps work without API key (shows simulation message)
- **Security**: API key loaded from environment variables (never hardcoded)

## 💡 Troubleshooting

### "Import google.generativeai could not be resolved"
- Run: `pip install google-generativeai`
- Make sure virtual environment is activated

### "No API key configured"
- Set environment variable: `export GEMINI_API_KEY="your-key"`
- Verify with: `echo $GEMINI_API_KEY`

### "Error calling Gemini API"
- Check your API key is valid (starts with AIza...)
- Verify you haven't exceeded rate limits (15 req/min free tier)
- Check internet connection

## 📚 Additional Resources

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

**Author**: AKINBOYEWA  
**Matric**: 23CG034029  
**Course**: NLP/AI Project