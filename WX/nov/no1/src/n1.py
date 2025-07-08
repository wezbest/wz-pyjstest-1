# ///////////////////////////////
# n1.pu = Testing out models
# ///////////////////////////////

# --- Imports ----

import os

from dotenv import load_dotenv
from openai import OpenAI
from rich import print as rpr

from .utz import he1

# --- Vars ----

load_dotenv("src/.azz")
NV_T = os.getenv("NOV")

# --- Main ----


def n1_main():
    te_mo()


# --- Subs ----

# Brinting envaz
def brint_env():
    he1("Brintaz Envaz")
    rpr(f"[bold green]NOV:[/bold green] {NV_T}")

# Testing Modelo


def te_mo():
    he1("Testing Models")

    modelz = [
        "google/gemma-3-1b-it",
        "qwen/qwen3-4b-fp8",
        "qwen/qwen2.5-7b-instruct",
        "meta-llama/llama-3.2-1b-instruct"
    ]

    quez = "What mean buty dance ?"

    base_url = "https://api.novita.ai/v3/openai"
    api_key = NV_T
    model = modelz[0]

    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    stream = True  # or False
    max_tokens = 1000

    response_format = {"type": "text"}

    chat_completion_res = client.chat.completions.create(
        model=model,
        messages=[

            {
                "role": "user",
                "content": quez,
            }
        ],
        stream=stream,
        extra_body={
        }
    )

    if stream:
        for chunk in chat_completion_res:
            rpr(chunk.choices[0].delta.content or "", end="")
    else:
        rpr(chat_completion_res.choices[0].message.content)
