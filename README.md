# Smart FAQ Chatbot (NLP-Powered)

This is a simple but effective chatbot I developed to handle customer queries automatically. It doesn't just search for keywords; it uses mathematical similarity to figure out the user's intent and provide the best answer from our dataset[cite: 5].

 How it Works
*   **The Brain**: The backend is built with Python and Flask, handling the logic and API requests[cite: 2].
*   **Text Processing**: When you type a question, the system uses NLTK to strip out "noise" and normalize words (like turning "running" into "run")[cite: 5].
*   **Smart Matching**: It uses TF-IDF and Cosine Similarity to compare your question against the FAQs and pick the answer with the highest "score"[cite: 5].
*   **The Interface**: A clean, responsive chat window built with HTML, CSS, and Vanilla JavaScript.

 My Project Structure
*   `app.py`: The core Flask app and API routes[cite: 2].
*   `matcher.py`: Where the vectorization and similarity math happens[cite: 5].
*   `preprocessor.py`: The pipeline for cleaning and lemmatizing text[cite: 5].
*   `faqs.py`: Our database of questions and answers[cite: 3].
*   `templates/`: Contains `index.html` (Make sure this folder exists for Flask to find the UI!)[cite: 1, 4].

# Getting it Started
1. Install what you need:
   ```bash
   pip install flask scikit-learn nltk numpy
