import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

# Initialize the OpenAI LLM model
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai.api_key)

# Define a simple prompt template for the chatbot
prompt_template = "You are a helpful assistant. Respond to the following message: {message}"

# Create the prompt using LangChain's PromptTemplate
prompt = PromptTemplate(input_variables=["message"], template=prompt_template)

# Set up the LLMChain, which will take in a user message and generate a response
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Function to run the chatbot
def run_chatbot():
    print("Chatbot: Hello! I am your chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        
        # Get the chatbot's response
        response = llm_chain.run(message=user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    run_chatbot()
