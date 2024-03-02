import pandas as pd

# Define the intents dictionary
intents = {
    "greetings": {
        "patterns": ["hi", "hello", "hey"],
        "responses": ["hello sir, how are you?", "welcome back sir", "Good day, sir"]
    },
    "application": {
        "patterns": ["open", "can you open", "start"],
        "responses": ["sure sir", "working on it sir", "on it sir", "certainly initiating"]
    },
    "how": {
        "patterns": ["how are you doing", "how are you jarvis", "are you there"],
        "responses": ["Great! sir", "I'm doing well, thank you!", "Fantastic sir"]
    },
    # Add more intents as needed
}

# Create lists to store patterns and intents
patterns = []
intents_list = []

# Extract patterns and intents from the intents dictionary
for intent, data in intents.items():
    for pattern in data['patterns']:
        patterns.append(pattern)
        intents_list.append(intent)

# Create a DataFrame to represent the dataset
dataset = pd.DataFrame({'Pattern': patterns, 'Intent': intents_list})

# Display the dataset
print(dataset)
