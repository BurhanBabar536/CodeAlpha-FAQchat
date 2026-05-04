import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faqs import faqs
from preprocessor import preprocess

# Preprocess all FAQ questions once at startup
faq_questions_clean = [preprocess(f["question"]) for f in faqs]
faq_answers = [f["answer"] for f in faqs]

def get_best_answer(user_input, threshold=0.2):
    user_input_clean = preprocess(user_input)

    # If user input is empty after cleaning
    if not user_input_clean.strip():
        return "Please type a proper question.", 0.0

    # Combine FAQ questions + user input for vectorization
    all_texts = faq_questions_clean + [user_input_clean]

    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # User input is the last row; compare it against all FAQ rows
    user_vector = tfidf_matrix[-1]
    faq_vectors = tfidf_matrix[:-1]

    # Calculate cosine similarity scores
    similarities = cosine_similarity(user_vector, faq_vectors).flatten()

    # Find the best matching FAQ
    best_index = np.argmax(similarities)
    best_score = similarities[best_index]

    if best_score >= threshold:
        return faq_answers[best_index], round(float(best_score), 2)
    else:
        return "Sorry, I couldn't find an answer to that. Please contact support@example.com.", 0.0