import re
import logging
import warnings
import os
from transformers import pipeline

# ----------------------------
# Silence warnings completely
# ----------------------------
warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "true"

logging.getLogger("transformers").setLevel(logging.ERROR)

# ----------------------------
# Load FLAN-T5-small
# ----------------------------
summarizer = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)


# ----------------------------
# Clean model output
# ----------------------------
def clean_text(text: str) -> str:
    """
    Clean unwanted artifacts from model output.
    """

    # Remove extra newlines
    text = re.sub(r"\n{2,}", "\n\n", text)

    # Remove "Summary:" prefix if present
    if text.lower().startswith("summary:"):
        text = text[len("summary:"):].strip()

    # Remove repeated spaces
    text = re.sub(r"\s{2,}", " ", text)

    # Remove trailing incomplete sentence fragments
    text = re.sub(r"\s+\.$", ".", text)

    return text.strip()


# ----------------------------
# Generate Summary
# ----------------------------
def generate_summary(text: str, max_length: int = 200) -> str:
    """
    Generate a high-quality summary using FLAN-T5-small
    with stronger coherence & repetition control.
    """

    word_count = len(text.split())

    if word_count < 40:
        return "Input text is too short to summarize."

    prompt = (
        "Provide a clear, concise, and non-repetitive summary of the following text. "
        "Focus on key facts, important statistics, causes, impacts, and conclusions.\n\n"
        f"{text}\n\n"
        "Summary:"
    )

    result = summarizer(
        prompt,
        max_new_tokens=max_length,
        min_new_tokens=80,
        do_sample=False,              # deterministic (best for summarization)
        num_beams=5,                  # better reasoning
        repetition_penalty=1.8,       # stronger repetition control
        no_repeat_ngram_size=4,       # prevents phrase repetition
        length_penalty=1.2,           # avoids too-short output
        early_stopping=True
    )

    summary = result[0]["generated_text"]

    return clean_text(summary)