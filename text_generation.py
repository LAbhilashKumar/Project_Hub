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
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DjkuZ-t9CDTJ",
        "outputId": "07e7721a-9057-435e-9919-7978d663e2cb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: transformers in /usr/local/lib/python3.10/dist-packages (4.37.2)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from transformers) (3.13.1)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.19.3 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.20.3)\n",
            "Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (1.25.2)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from transformers) (23.2)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (6.0.1)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (2023.12.25)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from transformers) (2.31.0)\n",
            "Requirement already satisfied: tokenizers<0.19,>=0.14 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.15.2)\n",
            "Requirement already satisfied: safetensors>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.4.2)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.10/dist-packages (from transformers) (4.66.2)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.19.3->transformers) (2023.6.0)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub<1.0,>=0.19.3->transformers) (4.9.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->transformers) (2024.2.2)\n"
          ]
        }
      ],
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
      "execution_count": 17,
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
      "execution_count": 20,
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
      "execution_count": 21,
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
      "execution_count": 22,
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
      "execution_count": 14,
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GwJJa3vnNyie",
        "outputId": "7a1776ed-c6af-47da-e00b-9e5fc4f364d2"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tensor([[   72,  1842,  6953,   582,    13,   198,   198,    40,  1101,   407,\n",
              "          1016,   284,  6486,   284,   345,    13,   314,  1101,   257,  3236,\n",
              "          4336,   286,  7931,  1869,    13,   679,   338,   530,   286,   616,\n",
              "          4004,  9048,  1492,  3435,    11,   290,   314,  1053,   587,   257,\n",
              "          4336,  1201,   314,   373,   257,  5141,    13,  1406,   618,   314,\n",
              "          1043,   503,   326,   339,   373,  2406,   736,   284,   262,  1263,\n",
              "          3159,    11,   314,  3521,   470,  4043,   284,   766,   644,   339,\n",
              "           561,   804,   588,   287,   262,  9923, 21932,  1512, 11950,    13,\n",
              "           632,   338,   257,  4320,  1282,  2081,   329,   502,   284,   307,\n",
              "          1498,   284,   670,   351,   683,   757,    11,   475,   340,   338]])"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
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
      "execution_count": 24,
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