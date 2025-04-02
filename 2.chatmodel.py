from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10) #bascially temprature means incrscing the accuracy like if we keep 0 to 0.3
#its good for task like coding maths and 0.7 to 1.5+ creativity )

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)
#to run the code write python (2.Chatmodels/2.chatmodel.py)