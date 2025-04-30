from google import genai

client = genai.Client(api_key="YOUR_API_KEY_HERE")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents='hey i am rafey'
)

print(response.text)

