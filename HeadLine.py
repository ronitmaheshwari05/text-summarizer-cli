import re
import logging
import warnings
import os
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ----------------------------
# Silence warnings
# ----------------------------
warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.getLogger("transformers").setLevel(logging.ERROR)

# ----------------------------
# Load FLAN-T5-Large
# ----------------------------
MODEL_NAME = "google/flan-t5-large"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


# ----------------------------
# Clean Output
# ----------------------------
def clean_output(text: str) -> str:
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = text.strip()

    if "HEADLINE:" in text.upper():
        text = text.split(":")[-1].strip()

    return text


# ----------------------------
# Reject weak headlines
# ----------------------------
def is_weak_headline(headline: str, original_text: str) -> bool:
    first_line = original_text.strip().split(".")[0].lower()
    first_words = " ".join(first_line.split()[:4])

    if headline.lower().startswith(first_words):
        return True

    if len(headline.split()) < 4:
        return True

    return False


# ----------------------------
# Tone Prompts
# ----------------------------
TONE_STYLES = {
    "neutral": "Maintain professional journalistic balance.",
    "analytical": "Adopt a structured analytical tone focused on strategy and economic implications.",
    "urgent": "Create urgency while maintaining credibility.",
    "market": "Emphasize financial, policy, and market consequences.",
    "optimistic": "Highlight progress, innovation, and opportunity without exaggeration.",
    "bloomberg": (
        "Write in a Bloomberg-style executive tone. "
        "Focus on capital flows, geopolitical positioning, regulatory shifts, "
        "corporate strategy, and macroeconomic consequences. "
        "Keep it sharp, authoritative, and globally contextual."
    )
}

# ----------------------------
# Generate Headline
# ----------------------------
def generate_headline(text: str, tone: str = "neutral"):

    if not text or len(text.split()) < 40:
        return "Input text too short."

    tone_instruction = TONE_STYLES.get(tone, TONE_STYLES["neutral"])

    prompt = (
    "You are a senior global financial news editor crafting a front-page headline.\n\n"

    "MISSION:\n"
    "Distill the article into a powerful, strategic, globally relevant headline.\n\n"

    "HEADLINE REQUIREMENTS:\n"
    "- Use decisive, active verbs.\n"
    "- Highlight strategic, economic, geopolitical, or structural consequences.\n"
    "- Sound authoritative and data-driven.\n"
    "- Avoid emotional exaggeration or fear-driven language.\n"
    "- Avoid generic words like 'technology', 'future', 'challenge', or 'impact'.\n"
    "- Do NOT repeat the opening words of the article.\n"
    "- Do NOT copy phrases directly.\n"
    "- Keep it between 6 and 10 words.\n"
    "- Make it read like Bloomberg, Reuters, or Financial Times.\n\n"

    f"TONE DIRECTIVE:\n{tone_instruction}\n\n"

    f"ARTICLE:\n{text}\n\n"
    "FINAL HEADLINE:"
)

    try:
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=18,
                do_sample=True,
                temperature=1.15,
                top_p=0.92,
                repetition_penalty=2.0,
                no_repeat_ngram_size=3,
                num_return_sequences=3
            )

        candidates = [
            clean_output(tokenizer.decode(o, skip_special_tokens=True))
            for o in outputs
        ]

        for headline in candidates:

            if not headline:
                continue

            headline = headline.strip()

            # Remove trailing non-alphanumeric character (incomplete punctuation)
            if headline and not headline[-1].isalnum():
                headline = headline[:-1]

            # Normalize spacing
            headline = " ".join(headline.split())

            if not is_weak_headline(headline, text):
                words = headline.split()
                if len(words) > 10:
                    headline = " ".join(words[:10])
                return headline

        return candidates[0] if candidates else "Headline generation failed."

    except Exception as e:
        return f"Generation error: {e}"