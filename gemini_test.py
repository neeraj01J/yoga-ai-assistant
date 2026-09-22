
from dotenv import load_dotenv
from google.genai.types import AutomaticFunctionCallingConfig
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the API key from the .env file
load_dotenv()

# Create the Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# Disable automatic function calling
model_without_afc = model.bind(
    automatic_function_calling=AutomaticFunctionCallingConfig(
        disable=True
    )
)

# Send a question to Gemini
response = model_without_afc.invoke(
    "Explain yoga in two simple sentences."
)

# Display a clean response
print("\nGemini Response:")

if isinstance(response.content, list):

    for item in response.content:

        if item.get("type") == "text":
            print(item.get("text", ""))

else:
    print(response.content)