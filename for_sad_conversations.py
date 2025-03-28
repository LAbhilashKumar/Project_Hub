# import random
# from transformers import pipeline
# import warnings
# import json
# # from sentiment_anal import sentence
#
# print("loading model")
# classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=0)
# print("at intents ")
# intents = [
#     "self_doubt", "peace_restlessness", "bad_times", "dharma",
#     "fear", "fear_of_rejection", "control_mind", "stop_negative_thoughts",
#     "overthinking", "duty", "procrastination", "positive_thinking", "happiness", "anger"
#     , "facing_difficult_times"
# ]
#
# print("getting predefined intents ")
#
#
# def get_intents(user_input, classifier, intents):
#     results = classifier(user_input, candidate_labels=intents)
#     return results['labels'][0]
#
#
#
# from sentiment_anal import sentence
# print(sentence)
# warnings.simplefilter("ignore")
# # user_input = input("enter here..")
# # from sentiment_anal import sentence
# detected_input = get_intents(sentence, classifier, intents)
# print("intents class....", detected_input)
# # a="self_doubt"
# with open("krishna_arjuna_conversations.json", "r") as file:
#     data = json.load(file)
# print(type(data))
# print(data[detected_input][random.randint(0, 2)])

