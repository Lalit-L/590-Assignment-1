import os
import requests


# Lalit Lakamsani
# Assignment 1, CYBERSEC 590 - AI


from dotenv import load_dotenv, find_dotenv

load_dotenv()

# Makes sure the env file exists

print(find_dotenv())

API_KEY = os.getenv("LITELLM_API_KEY")

API_BASE = os.getenv("LITELLM_API_BASE")

MODEL = os.getenv("LITELLM_MODEL")

# Checks to see that the Base, Model, and Key are properly loaded (doesn't display the actual key)

print("API_BASE: ", API_BASE)
print("MODEL: ", MODEL)
print("Key Loaded: ", API_KEY is not None)

print("\n\nBUG Fixer")
print("Paste your code below.")
print("Type END on a line by itself when finished.\n")

# Gets the input from the user

lines = []

while True:
	line = input()
	if line == "END":
		break
	lines.append(line)

code = "\n".join(lines)


# Context for the model, telling it what to do

messages = [
	{
		"role": "system",
		"content": (
			"You are a code reviewer. Find mistakes in the user's code. "
			"For each mistake, explain what is wrong, why it is wrong, "
			"and how to fix it. Do not invent problems. "
			"If the code looks correct, say so."
			" Be concise in your answers, do not overthink a problem too much, and"
			" provide explanations that are quick and simple to understand."
			" Avoid over-explaining."
		),
	},
	{
		"role": "user",
		"content": f"Find mistakes in this code:\n\n{code}",
	},
]


# Sends the response to the model, using the key and base provided
# Max tokens is 3k to ensure there's enough space for the model to reason and print out an answer

# Code was inspired from the Cybersec520 LLM's Via API Lab (Precursor to Assignment 2)
print("Sending Response")
resp = requests.post(
	f"{API_BASE}/v1/chat/completions",
	headers={"Authorization": f"Bearer {API_KEY}"},
	json={
		"model": MODEL,
		"messages": messages,
		"max_tokens": 3000,
		"temperature": 0.0,
	},
	timeout=60,
)
print("Recieved Response")

# Prints the response from the model

resp.raise_for_status()

result = resp.json()
print(result["choices"][0]["message"]["content"].strip())
