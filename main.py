import nltk
import re
import webbrowser
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import wikipedia

# Download necessary NLTK data
nltk.download('punkt')
nltk.download("wordnet")
nltk.download("stopwords")

def preprocess(text):
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize text
    tokens = nltk.word_tokenize(text.lower())
    # Remove stop words
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

responses = {
    "hi": "Hello, how can I help you?",
    "what is your name?": "My name is Chatbot.",
    "who created you?": "I was created by MuraKon.",
    "bye": "Goodbye!",
    "youtube": "opening youtube",
    "google":"opening google",
    "twitter":"opening twitter",
    "instagram":"opening Instagram",
    "facebook":"opening Facebook",
    "search": "searching on Wikipedia"
}

def generate_response(user_input):
    # Preprocess user input
    tokens = preprocess(user_input)
    # Check for known inputs
    for key in responses.keys():
        if key in tokens:
            if key == "youtube":
                webbrowser.open("https://www.youtube.com")
            elif key == "google":
                webbrowser.open("https://www.google.com")
            elif key == "twitter":
                webbrowser.open("https://www.twitter.com")
            elif key == "instagram":
                webbrowser.open("https://www.instagram.com")
            elif key == "facebook":
                webbrowser.open("https://www.facebook.com")
            elif key == "search":
                # Assuming the next token is the search query
                search_query = ' '.join(tokens[tokens.index(key) + 1:])
                try:
                    # Search Wikipedia and return the summary of the first result
                    result = wikipedia.summary(search_query, sentences=2)
                    return result
                except wikipedia.exceptions.DisambiguationError as e:
                    # Handle disambiguation error by returning the options
                    return str(e)
                except wikipedia.exceptions.PageError:
                    # Handle page error by informing the user
                    return "Sorry, I couldn't find any information on that topic."
            return responses[key]
    return "I'm sorry, I don't understand. Can you please rephrase?"

# Display instructions
print("Welcome to the Chatbot! Here's how you can interact with me:")
print("- Type 'hi' to greet me.")
print("- Ask 'what is your name?' to know my name.")
print("- Say 'who created you?' to learn about my creator.")
print("- Type 'bye' to end our conversation.")
print("- You can also ask me to open websites like 'youtube', 'google', 'twitter', 'instagram', or 'facebook'.")
print("- If you want to search something, type 'search' followed by your query.")
print("- To end the program, type 'q'.")


while True:
    user_input = input("You: ")
    # End program with 'q'
    if user_input.lower() == 'q':
        print("Goodbye!")
        break
    response = generate_response(user_input)
    print("Chatbot: " + response)

