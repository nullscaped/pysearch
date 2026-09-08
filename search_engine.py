import re

class SearchEngine:
    def __init__(self):
        self.documents = {}
        self.index = {}

    def search(self, query):
        words = re.findall(r"\b\w+\b", query.lower())

        scores = {}

        for word in words:
            if word in self.index:
                for document in self.index[word]:
                    if document not in scores:
                        scores[document] = 0

                    scores[document] += 1

        ranked_results = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return ranked_results

        return list(results)

    def add_document(self, name, text):
        self.documents[name] = text

        words = re.findall(r"\b\w+\b", text.lower())

        for word in words:
            if word not in self.index:
                self.index[word] = []

            if name not in self.index[word]:
                self.index[word].append(name)
