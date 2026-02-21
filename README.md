# 📰 HeadLine-Generator-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/Framework-HuggingFace-orange.svg" />
  <img src="https://img.shields.io/badge/Model-FLAN--T5--Large-yellow.svg" />
  <img src="https://img.shields.io/badge/Backend-PyTorch-red.svg" />
  <img src="https://img.shields.io/badge/Interface-CLI-green.svg" />
  <img src="https://img.shields.io/badge/OS-Mac%20%7C%20Windows%20%7C%20Linux-lightgrey.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success.svg" />
</p>

A transformer-powered AI Headline Generator built using Hugging Face Transformers and Google's FLAN-T5-Large model.

This project generates high-impact, newsroom-style headlines from long-form articles using advanced prompt engineering, tone conditioning, and controlled text generation.

---

## 🧠 Project Overview

This project demonstrates practical implementation of:

- Transformer-based NLP systems
- Prompt engineering with structured constraints
- Tone-conditioned headline generation
- Repetition control mechanisms
- Weak-output rejection logic
- CLI-based ML application design
- Efficient local model inference

The system transforms long articles into concise, professional, front-page style headlines.

---

## 🚀 Installation & Setup

### 🔧 Clone the Repository
```bash
git clone https://github.com/ronitmaheshwari05/HeadLine-Generator-CLI.git
cd HeadLine-Generator-CLI
```

### 🖥️ Create Virtual Environment

#### 🍎 Mac / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 🪟 Windows (PowerShell)
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📦 Requirements
```
transformers>=4.37.0
torch>=2.6.0
accelerate>=0.27.0
```

---

## ▶️ Usage

**Basic usage:**
```bash
python main.py "Paste your full article text here..."
```

**Using a tone mode:**
```bash
python main.py "Article text here..." --tone analytical
```

**Using file input:**
```bash
python main.py --file article.txt --tone market
```

---

## 🎭 Available Tone Modes

| Mode | Description |
|---|---|
| `neutral` | Professional newsroom balance |
| `analytical` | Bloomberg-style strategic and economic framing |
| `urgent` | Breaking-news intensity |
| `market` | Financial and policy emphasis |
| `optimistic` | Innovation-focused framing |

---

## 🤖 Model Configuration

- **Model:** `google/flan-t5-large`
- **Architecture:** Encoder-Decoder (Seq2Seq)
- **Backend:** PyTorch

**Generation Settings:**

- Sampling enabled
- Temperature: `1.15`
- Top-p: `0.92`
- Repetition Penalty: `2.0`
- No Repeat N-gram Size: `3`
- Multi-candidate generation
- Weak-headline rejection logic
- 6–10 word constraint enforcement

These configurations ensure:

- Strong action verbs
- Reduced copying from the article
- Professional newsroom tone
- Balanced creativity and coherence

---

## 🧪 Example

### 📥 Input
```
Major economies are investing billions into semiconductor manufacturing to reduce
reliance on overseas chip production and strengthen technological sovereignty.
```

### 📤 Output

**Analytical Mode:**
```
Nations Accelerate Drive for Chip Independence
```

**Market Mode:**
```
Governments Expand Billion-Dollar Semiconductor Push
```

---

## 📸 Demo

![CLI Demo](Demo.png)

---

## 📁 Project Structure
```
HeadLine-Generator-CLI/
│
├── main.py
├── HeadLine.py
├── requirements.txt
├── README.md
└── Demo.png
```

---

## 🚀 Future Improvements

- 💡 Multiple headline suggestions output
- 🏆 Headline ranking system
- 🗂️ Category-based generation (Finance, Tech, Policy)
- 🌐 Web-based interface
- 🐳 Docker deployment

---

## 🤝 Contributions

Contributions, feature suggestions, and improvements are welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Implement your improvements
4. Submit a Pull Request

---

## 👨‍💻 Author

**Ronit Maheshwari**  
B.Tech Computer Science (AI & ML)  
Machine Learning & MLOps Enthusiast

---

⭐ If you found this project useful, consider giving it a star!
