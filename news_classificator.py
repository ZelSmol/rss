import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


def predict_category(news_title: str) -> str:
    """
    Возращает категорию новости по заголовку
    """
    #
    category_list = ["sport", "world", "business",
                     "health", "entertainment", "sci_tech"]

    docs_new = [news_title]

    # Загружаем модель нейронной сети (softmax)
    loaded_vec = CountVectorizer(vocabulary=pickle.load(
        open("./neural_files/count_vector.pkl", "rb")))
    loaded_tfidf = pickle.load(open("./neural_files/tfidf.pkl", "rb"))
    loaded_model = pickle.load(open("./neural_files/softmax.pkl", "rb"))

    X_new_counts = loaded_vec.transform(docs_new)
    X_new_tfidf = loaded_tfidf.transform(X_new_counts)
    predicted = loaded_model.predict(X_new_tfidf)

    return category_list[predicted[0]]
