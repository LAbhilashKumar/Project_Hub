# -*- coding: utf-8 -*-
"""text_generation.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YS7gLBuGp8NdFPUuslWogjzoTPRyAiA5
"""

!pip install transformers

from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer=GPT2Tokenizer.from_pretrained("gpt2-large")

model=GPT2LMHeadModel.from_pretrained("gpt2-large",pad_token_id=tokenizer.eos_token_id)

sentence="i love iron man"
numeric_id=tokenizer.encode(sentence,return_tensors="pt")

numeric_id

result=model.generate(numeric_id, max_length=100,num_beams=5,no_repeat_ngram_size=2,early_stopping=True)
result

generated_Text=tokenizer.decode(result[0], skip_special_tokens=True)
print(generated_Text)