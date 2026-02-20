import re
import logging
import warnings
import os
import random
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

    # Remove incomplete trailing punctuation
    text = re.sub(r"\s+\.$", ".", text)

    return text.strip()


def generate_summary(text: str, max_length: int = 200) -> str:
    """
    Generate a high-quality abstractive summary using FLAN-T5-small
    with stronger variation and anti-copy behavior.
    """

    if len(text.split()) < 40:
        return "Input text is too short to summarize."

    styles = [
        "Rewrite the following content into a concise summary.",
        "Provide a professional abstract of the text.",
        "Summarize the key insights clearly.",
        "Explain the core information briefly.",
        "Create a short analytical summary."
    ]

    instruction = random.choice(styles)

    prompt = (
        f"{instruction}\n\n"
        "IMPORTANT:\n"
        "- Do NOT copy the first sentence.\n"
        "- Rephrase all content in your own words.\n"
        "- Avoid repeating phrases from the original text.\n\n"
        f"{text}\n\n"
        "Summary:"
    )

    result = summarizer(
        prompt,
        max_new_tokens=max_length,
        min_new_tokens=70,
        do_sample=True,              
        temperature=0.9,             
        top_p=0.95,
        repetition_penalty=1.8,
        no_repeat_ngram_size=4
    )

    return clean_text(result[0]["generated_text"])
