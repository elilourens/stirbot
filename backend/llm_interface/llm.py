import ollama


def chat(prompt, context, model='ministral-3', system_prompt=None, history=None):
    messages = []

    if system_prompt:
        messages.append({
            'role': 'system',
            'content': system_prompt
        })

    # Add conversation history (excluding the latest user message)
    if history:
        for msg in history:
            # Extract text from Gradio's rich text format
            content = msg['content']
            if isinstance(content, list):
                
                content = ''.join([item.get('text', '') for item in content if isinstance(item, dict)])

            messages.append({
                'role': msg['role'],
                'content': content
            })

    prompt_enigneered_message = f"Use this context: {context} to answer this user query: {prompt}"

    messages.append({
        'role': 'user',
        'content': prompt_enigneered_message
    })

    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']

