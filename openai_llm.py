from openai import OpenAI

system_prompt = """
You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.
"""

def create_openai_llm(prompt_template, llm_model):
    def F(text):
        # Point to the local server
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

        prompt = prompt_template.format(text=text)
        
        completion = client.chat.completions.create(
            model = llm_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.01,
        frequency_penalty = 1.5,
        )

        return extract_json(completion.choices[0].message.content)

    return F

def call_llm(text):
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    prompt = prompt_template.format(text=text)
    
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ],
    temperature=0.01,
    )

    return extract_json(completion.choices[0].message.content)

def extract_json(text):
    lines = text.split("\n")
    start = False
    
    results=''
    
    for l in lines:
        if l.startswith("```"):
            if start is False:
                start = True
                continue
            else:
                start = False
                return results
        if start:
            results = results + l
    
    return results