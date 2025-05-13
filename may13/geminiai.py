import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

# Verify if the API key is loaded (for debugging)
if api_key:
    print("API_KEY loaded successfully.")
else:
    print("API_KEY not found. Make sure you have a .env file with API_KEY=YOUR_ACTUAL_API_KEY")

genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    print(f"Error initializing the model: {e}")
    model = None  # Set model to None if initialization fails

# Text generation
def generate_text(prompt):
    if model:
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating text: {e}"
    else:
        return "Model not initialized. Cannot generate text."

# Text summarization
def summarize_text(text):
    if model:
        prompt = f"Summarize the following text:\n\n{text}"
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error summarizing text: {e}"
    else:
        return "Model not initialized. Cannot summarize text."

def main():
    if model:
        # Example usage
        prompt = "What is the capital of France?"
        response = generate_text(prompt)
        print("Response:", response)

        text = "Gemini is a new AI model developed by Google. It is designed to be more efficient and powerful than previous models. It has shown promising results in various benchmarks and is expected to have a significant impact on the field of artificial intelligence."
        summary = summarize_text(text)
        print("Summary:", summary)
    else:
        print("The main function cannot run because the model was not initialized.")

if __name__ == "__main__":
    main()