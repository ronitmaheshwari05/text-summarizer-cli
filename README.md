# 🧠 Text Summarizer CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/Framework-HuggingFace-orange.svg" />
  <img src="https://img.shields.io/badge/Model-FLAN--T5--Small-yellow.svg" />
  <img src="https://img.shields.io/badge/Backend-PyTorch-red.svg" />
  <img src="https://img.shields.io/badge/Interface-CLI-green.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success.svg" />
</p>

A lightweight, transformer-powered Command-Line Text Summarizer built using Hugging Face Transformers and Google’s FLAN-T5 model.

This project demonstrates practical understanding of:
- Transformer-based NLP systems  
- Prompt engineering  
- Beam search decoding  
- Repetition control mechanisms  
- CLI application design  
- Efficient local model inference  

---

# 🚀 Installation, Setup, Requirements, Usage, Model Configuration, Example, Output, Project Structure, Demo & Author

## 🔧 Clone Repository & Setup Environment

```bash
git clone https://github.com/ronitmaheshwari05/text-summarizer-cli.git
cd text-summarizer-cli

python3 -m venv venv
source venv/bin/activate

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

Run the CLI tool directly from terminal:

```bash
python main.py "Paste your long article text here..."
```

What happens internally:

- Accepts long-form text input
- Uses FLAN-T5 for abstractive summarization
- Applies beam search for stable output
- Controls repetition with n-gram blocking
- Cleans artifacts from model output
- Displays structured summary in terminal

---

## 🤖 Model Configuration

- Model: `google/flan-t5-small`
- Pipeline: `text2text-generation`
- Beam Search: `num_beams=5`
- Repetition Penalty: `1.6`
- No Repeat N-gram Size: `3`
- Deterministic Mode: `do_sample=False`
- Early Stopping: Enabled
- Length Control: `max_new_tokens` & `min_new_tokens`

These configurations ensure:

- Stable generation  
- Reduced redundancy  
- Structured compression  
- Improved coherence  

---

## 🧪 Example

### 📥 Input

```
Artificial Intelligence is transforming healthcare by enabling predictive analytics, improving diagnostic accuracy, and automating administrative workflows. It helps hospitals optimize resources and supports personalized treatment plans.
```

### 📤 Output

```
Artificial Intelligence is revolutionizing healthcare through predictive analytics and automation. It enhances diagnostic accuracy, optimizes hospital resource allocation, and supports personalized treatment strategies while improving overall patient outcomes.
```

---

## 📁 Project Structure

```
text-summarizer-cli/
│
├── main.py
├── summarizer.py
├── requirements.txt
├── README.md
└── venv/ (excluded from GitHub)
```

---

## 📸 Demo

![CLI Demo](Demo.png)

---

## 📝 How To Use

1. Open terminal inside project directory  
2. Type:

```bash
python main.py "Your long text here..."
```

Important:

- Always wrap input text inside double quotes  
- Press Enter  
- Summary will be generated instantly in terminal  

---

## 🚀 Upcoming Features

Planned enhancements:

- 💾 Save generated summaries to local file  
- 📂 View saved summaries  
- 📊 Display word count of output  
- ⏱ Show execution time  
- 🎯 Short / Medium / Long summary modes  
- 📄 File-based input support  
- 🧪 Evaluation metrics (ROUGE scoring)  
- ⚡ Performance benchmarking  

---

## 🎯 Technical Highlights

- Implemented abstractive summarization using instruction-tuned transformer
- Optimized decoding strategy with beam search
- Controlled hallucination & repetition using penalty mechanisms
- Built lightweight inference pipeline for CPU-based systems
- Designed modular CLI-based NLP application

---

## 👨‍💻 Author

Ronit Maheshwari  
B.Tech Computer Science (AI & ML)  
Machine Learning & MLOps Enthusiast  

---

⭐ If you found this project useful, consider giving it a star!
