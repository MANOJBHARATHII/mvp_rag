from langchain_google_genai._common import GoogleGenerativeAIError

from config import engine


def main():
    count = engine._collection.count()
    print(f"Indexed chunks: {count}")

    if count == 0:
        print("No documents are indexed. Run `uv run python injest.py` first.")
        return

    query = "What is the difference between a virus and bacteria?"
    try:
        results = engine.similarity_search(query, k=3)
    except GoogleGenerativeAIError as error:
        if "429" in str(error) or "RESOURCE_EXHAUSTED" in str(error):
            print(
                "Gemini embedding quota is exhausted. "
                "The partial index is intact; quota should reset before the next search."
            )
            return
        raise

    for index, document in enumerate(results, start=1):
        print(f"\nResult {index}:")
        print(document.page_content[:500])


if __name__ == "__main__":
    main()