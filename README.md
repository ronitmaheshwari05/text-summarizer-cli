# 🧠 Text Summarizer CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/Framework-HuggingFace-orange.svg" />
  <img src="https://img.shields.io/badge/Model-FLAN--T5--Small-yellow.svg" />
  <img src="https://img.shields.io/badge/Backend-PyTorch-red.svg" />
  <img src="https://img.shields.io/badge/Interface-CLI-green.svg" />
  <img src="https://img.shields.io/badge/OS-Mac%20%7C%20Windows%20%7C%20Linux-lightgrey.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success.svg" />
</p>

A lightweight, transformer-powered Command-Line Text Summarizer built using Hugging Face Transformers and Google's FLAN-T5 model.

This project demonstrates practical implementation of:

- Transformer-based NLP systems  
- Prompt engineering  
- Beam search decoding  
- Repetition control mechanisms  
- CLI-based ML application design  
- Efficient local model inference  

---

# 🚀 Installation, Setup, Requirements, Usage, Model Configuration, Example, Output, Project Structure & Author

---

## 🔧 Clone the Repository (Mac / Linux / Windows)

```bash
git clone https://github.com/ronitmaheshwari05/text-summarizer-cli.git
cd text-summarizer-cli
```

---

## 🖥️ Virtual Environment Setup

### 🍎 Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 🪟 Windows (PowerShell)

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

Run the CLI tool:

```bash
python main.py "Paste your long article text here..."
```

The system will:

- Accept long-form text input  
- Perform abstractive summarization using FLAN-T5  
- Apply beam search for stable decoding  
- Control repetition using n-gram blocking  
- Output a clean structured summary in the terminal  

---

## 🤖 Model Configuration

- Model: `google/flan-t5-small`
- Pipeline: `text2text-generation`
- Beam Search: `num_beams=5`
- Repetition Penalty: `1.6`
- No Repeat N-gram Size: `3`
- Deterministic Mode: `do_sample=False`
- Early Stopping Enabled
- Output Length Control via `max_new_tokens`

These configurations ensure:

- Stable generation  
- Reduced redundancy  
- Improved coherence  
- Balanced compression  

---

## 🧪 Example

### 📥 Input

```
Artificial Intelligence is transforming healthcare by enabling predictive analytics, improving diagnostic accuracy, and automating administrative workflows.
```

### 📤 Output

```
Artificial Intelligence is reshaping healthcare through predictive analytics and automation, enhancing diagnostic precision and optimizing operational efficiency.
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
├── Demo.png
└── venv/ (excluded from GitHub)
```

---

## 📸 Demo

![CLI Demo](Demo.png)

---

## 🚀 Upcoming Features

- 💾 Save generated summaries  
- 📂 View saved summaries  
- 📊 Word count display  
- ⏱ Execution time measurement  
- 🎯 Adjustable summary length modes  
- 📄 File-based input support  
- 📈 Evaluation metrics (ROUGE scoring)  

---

## 🤝 Contributions

Contributions, feature suggestions, and improvements are welcome.

If you would like to improve this project:

1. Fork the repository  
2. Create a new branch  
3. Implement your improvements  
4. Submit a Pull Request  

If you suggest meaningful updates or optimizations, feel free to open a PR.

---

## 👨‍💻 Author

Ronit Maheshwari  
B.Tech Computer Science (AI & ML)  
Machine Learning & MLOps Enthusiast  

---

⭐ If you found this project useful, consider giving it a star!
