from config import embedding_model, engine

search=engine.similarity_search("What is the difference between a virus and bacteria?", k=3)
print(search)