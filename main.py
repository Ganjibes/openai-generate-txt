import openai
import sys
import os
import openai

openai.api_key = ''

model = "text-davinci-003"
max_tokens = 850

keyword = sys.argv[1]
print('CLI param: ', keyword)

language = 'Ukrainian'
#keyword = 'Python'

prompt = f"Create 5 example sentences in {language} language containing keyword {keyword}. \
For each sentence show transcription to romaji and translation to English. \
Example sentences should be medium length, sometimes even longer. \
Output format should be: \
japanese keyword | \
Kanji: japanese sentence | \
Romaji: romaji transcription | \
Translation: english translation | \
"

response = openai.Completion.create(
    engine=model, 
    prompt=prompt, 
    max_tokens=max_tokens, 
    n=1, 
    stop=None, 
    temperature=0.4,
    top_p=1.0,
    frequency_penalty=0.3,
    presence_penalty=0.0,
)

#print('--- Response payload: ---')
#print(response)
#print()

#print('--- Prompt: ---')
#print(prompt)
#print()

# parse the response payload dictionary and printout the output
print('--- Response text: ---')
print(response["choices"][0]["text"].strip())
