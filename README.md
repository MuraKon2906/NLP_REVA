# Chatbot Project 🤖

Welcome to the Chatbot Project! This project is designed to create a simple yet powerful chatbot that can interact with users, perform searches on Wikipedia, and open various websites. The chatbot is built using Python and leverages the Natural Language Toolkit (NLTK) for text processing.

## Features 🌟

- **Greeting and Basic Queries**: The chatbot can greet the user, answer basic questions like its name and creator, and bid farewell.
- **Website Navigation**: It can open popular websites like YouTube, Google, Twitter, Instagram, and Facebook.
- **Wikipedia Search**: Users can ask the chatbot to search for information on Wikipedia by typing "search" followed by their query.
- **Error Handling**: The chatbot gracefully handles errors, such as disambiguation errors on Wikipedia and page errors.

## Getting Started 🚀

To get started with this project, you'll need Python installed on your system. The project uses the NLTK library, so you'll need to install it along with some additional data packages.

1. **Install Python**: If you haven't already, download and install Python from the [official website](https://www.python.org/downloads/).

2. **Install NLTK and Required Data Packages**: Open your terminal or command prompt and run the following commands:

```bash
pip install nltk
python -m nltk.downloader punkt wordnet stopwords
```

3. **Clone the Repository**: Clone this repository to your local machine.

4. **Run the Chatbot**: Navigate to the project directory in your terminal or command prompt and run the following command:

```bash
python main.py
```

## Usage 🛠️

Once the chatbot is running, you can interact with it by typing your queries or commands. Here are some examples:

- **Greeting**: Type `hi` to greet the chatbot.
- **Basic Queries**: Ask `what is your name?` or `who created you?`.
- **Website Navigation**: Type `youtube`, `google`, `twitter`, `instagram`, or `facebook` to open the corresponding website.
- **Wikipedia Search**: Type `search` followed by your query to search Wikipedia.
- **Ending the Conversation**: Type `bye` to end the conversation.
