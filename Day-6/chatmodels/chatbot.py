from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
load_dotenv()
model = ChatMistralAI(model = "mistral-small-2506", temperature = 0.9)
# here we are not saving our chat history bot dont know previous conversation 
# to save chat history we here created list and for more clarity can use dictionary
# but for a long chat its a problem of storage so we have messages in langchain = AIMessage, SystemMessage, HumanMessage
# and we can also select the mode of ai

print("Choose the AI mode")

messages = [
    SystemMessage(content = "You are a funny AI Agent")
]
while True:
    print("===== Enter 0 to Exit =====")
    prompt = input("You : ")
    messages.append(prompt)
    if(prompt == "0"):
        print("GoodBye !")
        break
    if prompt == "0":
        print("Goodbye!")
        break
        
    #Append as a proper HumanMessage object
    messages.append(HumanMessage(content=prompt))
    
    #Send the structured history to the model
    response = model.invoke(messages)
    
    #Append the response as an AIMessage object
    messages.append(AIMessage(content=response.content))
    
    print("Bot :", response.content)
