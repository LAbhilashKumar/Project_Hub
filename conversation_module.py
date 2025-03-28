from transformers import pipeline
from sentence_transformers import SentenceTransformer
import warnings

# from basicJarvis import speak
warnings.simplefilter("ignore")
print("about to load sentence transformers ")
model = SentenceTransformer("all-MiniLM-L6-v2")
# Define the summarization pipeline
# print("about to load summarixation ")
# summ = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

#
import ollama

# while True:
# def convo(x):
#     complete_response=""
#     client = ollama.Client()
#
#     model = "jarvis1"
#     prompt = x
#     # Stream response to print faster
#     response = client.generate(model=model, prompt=prompt, stream=True)
#
#     for part in response:
#         # print(part["response"], end="", flush=True)
#         complete_response+=part["response"]
#     print(complete_response)
#
#     print("response completed..")

# #     return output_text
# while True:
#     print(convo(input("enter here")))
# from langchain_community.llms import Ollama
#
# # Initialize the Ollama model
# ollama_model = Ollama(model="llama2")
# # Removed 'url_base'
# # Define the input prompt
# while True:
#     prompt = input("enter here")
#
#     # Get the model's response
#     response = ollama_model.invoke(prompt)
#
#     # Print the response
#     print(response)
#

# from langchain_community.llms import Ollama
#
# # Connect to the running Ollama server (No reloading!)
# ollama_model = Ollama(model="llama2", base_url="http://localhost:11434")
#
#
#
# def get_stream_response(prompt):
#     """Stream response (prints word-by-word like CMD)."""
#     for chunk in ollama_model.stream(prompt):
#         print(chunk, end="", flush=True)  # No delay, prints immediately
#
# # Example Usage:
# print("Response (Direct):")
# print(get_response("Explain AI in simple terms."))  # Direct response
#
# print("\nResponse (Streaming):")
# get_stream_response("Tell me a joke.")  # Word-by-word output


import ollama
import time
import random

# Predefined responses for different time delays with a
import ollama
import time
import random

# Predefined responses for different time delays
gap_fillers = {
    "processing": [
        "Analyzing your request in detail... Please stand by while I gather the necessary information.",
        "Processing your input... This won't take long, but I'm making sure to get the most relevant response.",
        "Retrieving the best possible information for you... Stay tuned while I dig deeper into my knowledge base.",
        "Computing an accurate response... This may take a few moments as I carefully generate a meaningful answer.",
        "Scanning through my database of knowledge... Almost ready to provide you with a well-informed reply."
    ],

    "almost": [
        "The response generation is nearly complete... Just finalizing the last details to ensure accuracy.",
        "Finalizing all the necessary details... Hold on a moment while I refine the output for you.",
        "Almost there... Optimizing my response to give you the best possible answer.",
        "Just a moment... Making sure everything is accurate before presenting my final answer.",
        "Verifying all retrieved data... Preparing to deliver a precise and well-structured response."
    ]
}


def convo(x, speak):
    complete_response = ""
    client = ollama.Client()
    model = "jarvis1"
    prompt = x

    start_time = time.time()
    response = client.generate(model=model, prompt=prompt, stream=True)

    shown_messages = set()  # Track displayed messages to avoid repetition

    print("\nGenerating response...\n")

    for part in response:
        elapsed_time = time.time() - start_time

        # Show filler messages at certain time thresholds
        if 7 < elapsed_time < 7.5 and "processing" not in shown_messages:
            speak(random.choice(gap_fillers["processing"]))
            shown_messages.add("processing")

        elif 14 < elapsed_time < 14.5 and "almost" not in shown_messages:
            speak(random.choice(gap_fillers["almost"]))
            shown_messages.add("almost")

        complete_response += part["response"]

    speak(complete_response)
    print("\nResponse completed.")
    # speak("")

# Example usage
# convo("ho are you?", print)
