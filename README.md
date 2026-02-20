# 🧠 Text Summarizer CLI

A lightweight and efficient command-line Text Summarizer built using Hugging Face Transformers and Google's FLAN-T5 model. This tool allows users to input long-form text directly through the terminal and generate a concise, structured, and non-repetitive summary using a transformer-based language model.

---

## 🚀 Installation, Setup, Requirements, Usage, Model Configuration, Example, Output, Project Structure & Author

### Clone the Repository and Setup Environment

```bash
git clone https://github.com/ronitmaheshwari05/text-summarizer-cli.git
cd text-summarizer-cli

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

### Requirements

```
transformers>=4.37.0
torch>=2.6.0
accelerate>=0.27.0
```

---

### Usage

Run the CLI tool:

```bash
python main.py "Paste your long article text here..."
```

The program:
- Processes input text
- Applies transformer-based summarization
- Controls repetition
- Prints a clean structured summary in the terminal

---

### Model Configuration

- Model: `google/flan-t5-small`
- Pipeline: `text2text-generation`
- Beam Search (`num_beams=5`)
- Repetition Penalty
- No Repeat N-gram Blocking
- Deterministic Generation (`do_sample=False`)
- Output Length Control (`max_new_tokens`, `min_new_tokens`)

These settings ensure stable, coherent, and non-repetitive summaries.

---

### Example

#### Input

```
Artificial Intelligence is transforming healthcare by enabling predictive analytics, improving diagnostic accuracy, and automating administrative workflows. It helps hospitals optimize resources and supports personalized treatment plans.
```

#### Output

```
Artificial Intelligence is revolutionizing healthcare through predictive analytics and automation. It enhances diagnostic accuracy, optimizes hospital resource allocation, and supports personalized treatment approaches while improving overall patient outcomes.
```

---

### Project Structure

```
text-summarizer-cli/
│
├── main.py
├── summarizer.py
├── requirements.txt
├── README.md
└── venv/ (not pushed to GitHub)
```

---


---

## 📸 Demo

![CLI Demo](Demo.png)

---


### 📝 How to Use

To generate a summary, type the input text inside double quotes and press Enter:

```bash
python main.py "Your long input text goes here..."
```

Make sure the entire input text is enclosed within double quotes.  
After pressing Enter, the model will process the text and generate a structured summary in the terminal.

---

## 🚀 Upcoming Features

Future updates will include:

- 💾 Save generated summaries to local files  
- 📂 View previously saved summaries  
- 📊 Display word count of the generated summary  
- ⏱ Show time taken to generate the summary  
- 🎯 Summary length modes (short / medium / long)  
- 📄 File input support  

Stay tuned for improvements as the project evolves.

### Author

Ronit Maheshwari  
B.Tech Computer Science (AI & ML)

---

⭐ If you found this project useful, consider giving it a star.
