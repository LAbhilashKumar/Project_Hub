from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, BlenderbotTokenizer, \
    BlenderbotForConditionalGeneration
from scipy.special import softmax
import warnings
import random
import json


# execution starts from here....
def sentiment(x,speak):
    warnings.simplefilter("ignore")  # to clear warning msgs
    sentence = x
    print("from while true..", sentence)
    # if sentence == "bye" or "see you later ":

    # load the model form hugging face
    model = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModelForSequenceClassification.from_pretrained(model)

    # converting input text into tokens
    encoded_text = sentence
    usertext = tokenizer(encoded_text, return_tensors="pt")

    # passing tokens to the model and storing raw o/p
    output = model(**usertext)
    scores = output.logits.detach().numpy()[0]

    # converting raw o/p into probabilities
    prob = softmax(scores)
    # print(f"probability scores {prob}")
    sentiment = ["Negative", "Neutral", "positive"]
    # scores.argmax() ->  returns highest probability's index
    predictedscore = sentiment[scores.argmax()]
    print(predictedscore)
    if predictedscore == "Negative":
        # loading model....
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)
        with open("krishna_arjuna_conversations.json", "r") as file:
            data = json.load(file)
        print("loading model")
        intents = [
            "self_doubt", "peace_restlessness", "bad_times", "uncontrolled_mind",
            "fear", "fear_of_rejection", "control_mind", "stop_negative_thoughts",
            "overthinking", "duty", "procrastination", "demotivation", "losing_hope", "anger"
            , "facing_difficult_times"
        ]

        def get_intents(user_input, classifier, intents):
            results = classifier(user_input, candidate_labels=intents)
            return results['labels'][0]
        warnings.simplefilter("ignore")
        detected_input = get_intents(sentence, classifier, intents)
        print("intents class....", detected_input)
        # print(data[detected_input][random.randint(0, 2)])
        a = data[detected_input][random.randint(0, 2)]
        # temp=""
        temp=a["quote"]+ "how to control "+" " +a["how_to_implement"]
        speak(temp)

# sentiment("sometimes i feel like demotivated to do work ")


#
# import torch
# import torchvision
# print(torch.__version__, torchvision.__version__)
#
# import torch
# print(torch.cuda.is_available())  # Should print True if a GPU is available
# print(torch.cuda.device_count())  # Should print the number of GPUs
# print(torch.cuda.get_device_name(-1))  # Should print GPU name if available
