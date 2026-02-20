import argparse
from summarizer import generate_summary


def main():
    parser = argparse.ArgumentParser(
        description="CLI Text Summarizer using FLAN-T5"
    )

    parser.add_argument(
        "text",
        type=str,
        help="Input text to summarize"
    )

    parser.add_argument(
        "--length",
        type=int,
        default=150,
        help="Maximum summary length"
    )

    args = parser.parse_args()

    print("\nGenerating Summary...\n")

    try:
        summary = generate_summary(
            text=args.text,
            max_length=args.length
        )

        print("Summary:\n")
        print(summary)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()