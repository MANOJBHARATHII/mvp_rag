from config import engine, llm
from langchain_google_genai._common import GoogleGenerativeAIError


def knowledge_based_chat(query):
    try:
        return engine.similarity_search(query, k=3)
    except GoogleGenerativeAIError as error:
        if "429" in str(error) or "RESOURCE_EXHAUSTED" in str(error):
            raise RuntimeError(
                "Gemini embedding quota is exhausted. "
                "Wait for quota to reset, then run the query again."
            ) from error
        raise


def chatbot(query):
    results = knowledge_based_chat(query)
    if not results:
        return "I could not find relevant information in the indexed documents."

    search_content = "\n\n".join(
        document.page_content for document in results
    )

    system_prompt = """You are a helpful assistant that answers questions based on the context provided.
If you don't know the answer, just say you don't know.
User question:
{query}
The content you have is:
{search_content}
Do not try to make up an answer."""

    prompt = system_prompt.format(
        query=query,
        search_content=search_content,
    )
    return llm.invoke(prompt)


if __name__ == "__main__":
    try:
        response = chatbot(
            "What is the difference between a virus and bacteria?"
        )
        if hasattr(response, "content"):
            print(response.content.encode("ascii", "replace").decode("ascii"))
        else:
            print(response)
    except RuntimeError as error:
        print(error)
