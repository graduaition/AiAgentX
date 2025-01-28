import anthropic
import openai
import google.generativeai as genai

class LLMClient:
    def __init__(self, llm_type, api_key):
        self.llm_type = llm_type
        self.api_key = api_key

    def generate_text(self, prompt):
        if self.llm_type == "claude":
            client = anthropic.Client(self.api_key)
            response = client.completion(prompt=f"{anthropic.HUMAN_PROMPT} {prompt} {anthropic.AI_PROMPT}", model="claude-2", max_tokens_to_sample=1000)
            return response["completion"]
        elif self.llm_type == "chatgpt":
            openai.api_key = self.api_key
            response = openai.Completion.create(model="gpt-4", prompt=prompt, max_tokens=1000)
            return response.choices[0].text
        elif self.llm_type == "gemini":
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        else:
            raise ValueError("Unsupported LLM")
