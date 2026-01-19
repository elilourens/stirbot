import ollama


def chat(prompt,context, model = 'ministral-3', system_prompt = None,):
    messages = []
    prompt_enigneered_message = f"Use this context: {context} to answer this user query: {prompt}"

    if system_prompt:
        messages.append({
            'role': 'system',
            'content': system_prompt
        })

    messages.append({
        'role': 'user',
        'content': prompt_enigneered_message
    })

    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']

