
import openai

openai.api_key = 'your_openai_api_key'

def generate_personalized_content(user_preferences):
    prompt = f"Generate a personalized content for a user interested in {user_preferences}."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    
    return response.choices[0].text.strip()

user_preferences = "technology, AI, and machine learning"
generated_content = generate_personalized_content(user_preferences)
print("Recommended Content:", generated_content)
