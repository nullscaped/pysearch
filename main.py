from search_engine import SearchEngine

engine = SearchEngine()

engine.add_document(
    "doc1.txt",
    "Python is a programming language used for backend development."
)

engine.add_document(
    "doc2.txt",
    "Chess is a strategy game with multiplayer servers."
)

engine.add_document(
    "doc3.txt",
    "Node.js can be used to create multiplayer applications."
)

print(engine.search("multiplayer servers"))