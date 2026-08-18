import os
from dotenv import load_dotenv
from litellm import completion


load_dotenv(override=True)
with open('langchain&LiteLLM\hamlet.txt','r',encoding='utf-8') as f:
    ham = f.read()
    

loc = ham.find('Speak, man')
print(ham[loc:loc+100])

key = os.getenv('GEMINI_API_KEY')
# define messages list used below
question = [{
    'role': 'user',
    'content': 'In Hamlet, when Laertes asks "Where is my father?" what is the reply?'
}]

# initial call (optional) using the question variable
# litlellm_gem = completion(model='gemini/gemini-2.5-flash', gemini_api_key=key, messages=question)


# print(litlellm_gem.choices[0].message.content)
# print(f"Input tokens: {litlellm_gem.usage.prompt_tokens}")
# print(f"Output tokens: {litlellm_gem.usage.completion_tokens}")
# print(f"Total tokens: {litlellm_gem.usage.total_tokens}")

print(f"To add in the prompt\n")

question[0]["content"] += "\n\nFor context, here is the entire text of Hamlet:\n\n" + ham

# call again with the full context
litlellm_gem = completion(model='gemini/gemini-2.5-flash', gemini_api_key=key, messages=question)
print(litlellm_gem.choices[0].message.content)