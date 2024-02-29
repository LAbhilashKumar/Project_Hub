{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyPFQvuga7hrYHjv9V3lnlfK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LAbhilashKumar/Project_Hub/blob/main/text_generation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DjkuZ-t9CDTJ"
      },
      "outputs": [],
      "source": [
        "!pip install transformers"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from transformers import GPT2Tokenizer, GPT2LMHeadModel"
      ],
      "metadata": {
        "id": "OpbIYrA-IZB8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tokenizer=GPT2Tokenizer.from_pretrained(\"gpt2-large\")"
      ],
      "metadata": {
        "id": "JmoXdIlFNeAW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model=GPT2LMHeadModel.from_pretrained(\"gpt2-large\",pad_token_id=tokenizer.eos_token_id)"
      ],
      "metadata": {
        "id": "kgJyITCjNl-U"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sentence=\"i love iron man\"\n",
        "numeric_id=tokenizer.encode(sentence,return_tensors=\"pt\")"
      ],
      "metadata": {
        "id": "szmwfBa1NtdW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numeric_id"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LKpwDdxVNwKq",
        "outputId": "55f2fc6e-dd9b-4556-9be5-584825340a2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[  72, 1842, 6953,  582]])"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result=model.generate(numeric_id, max_length=100,num_beams=5,no_repeat_ngram_size=2,early_stopping=True)\n",
        "result"
      ],
      "metadata": {
        "id": "GwJJa3vnNyie"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "generated_Text=tokenizer.decode(result[0], skip_special_tokens=True)\n",
        "print(generated_Text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vzsRKmC5N3Uz",
        "outputId": "4e30ef17-b4f2-40c9-8177-993ee13dd3da"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i love iron man.\n",
            "\n",
            "I'm not going to lie to you. I'm a huge fan of Iron Man. He's one of my favorite comic book characters, and I've been a fan since I was a kid. So when I found out that he was coming back to the big screen, I couldn't wait to see what he would look like in the Marvel Cinematic Universe. It's a dream come true for me to be able to work with him again, but it's\n"
          ]
        }
      ]
    }
  ]
}