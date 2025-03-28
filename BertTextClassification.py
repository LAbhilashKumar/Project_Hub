from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf

# Load model and tokenizer
model_dir = "C://Users//ABHILASH//OneDrive//Desktop//Jarvis//bert_testing//bert_classification_model"
model = TFAutoModelForSequenceClassification.from_pretrained(model_dir)
tokenizer = AutoTokenizer.from_pretrained(model_dir)

label_mapping = {0: "Internet Query", 1: "Automation", 2: "Conversation"}


def classify_text(text):
    inputs = tokenizer(text, return_tensors="tf", truncation=True, padding=True, max_length=512)
    logits = model(**inputs).logits
    return label_mapping.get(tf.argmax(logits, axis=1).numpy()[0], "Unknown")


# Test sentences


# Predict categories
# for sentence in test_sentences:
    # if classify_text((sentence)) == "Internet Query":
    #     print(f"{sentence}  Conversation")
    # elif classify_text((sentence)) == "Conversation":
    #     print(f"{sentence}  Internet Query")
    # else:
    #     print(f"Text: {sentence} | 🏷️ Category: {classify_text(sentence)}")
