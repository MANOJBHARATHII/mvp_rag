from config import engine, llm


def knowledge_based_chat(query):
    return engine.similarity_search(query, k=3)


def chatbot(query):
    results = knowledge_based_chat(query)
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
    response = chatbot(
        "What is the difference between a virus and bacteria?"
    )
    print(response.content.encode("ascii", "replace").decode("ascii"))
