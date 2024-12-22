import google.generativeai as genai

genai.configure(api_key="AIzaSyChfr36Ypjuz_2i9DvFCrDlE5Ya2xGjHIg")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how to become an Engineering manager?")
print(response.text)