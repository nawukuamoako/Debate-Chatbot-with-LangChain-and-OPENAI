from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool

load_dotenv()

class DebateResponse(BaseModel):
    your_stance_fact_check: str | None
    my_argument: str

# Initialize LLM and parser
llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=DebateResponse)

# Input for worldview stance
print("Welcome to the Debate Chatbot!")
topic = input("What is the topic of the debate? ")
your_stance = input("Are you for or against the topic? (For, Against): ")

if your_stance.lower() not in ["for", "against"]:
    print("Invalid input. Please enter 'For' or 'Against'.")
    exit()

if your_stance.lower() == "for":
    my_stance = "against"
else:
    my_stance = "for"

# Define prompt with placeholders for dynamic content
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
        """
        You are a chatbot designed to engage in debates on various topics.
        You are currently defending the {my_stance} stance on the topic of {topic}.
        If you do not have a strong or solid defense for a particular aspect of the topic, openly admit this and explain the reasons why.
        Maintain a logical, respectful, and coherent tone throughout the debate, ensuring that the conversation flows naturally.
        Be sure to address the user's question fully, providing a clear and reasoned response, and keep the discussion on track.
        Wrap your response in the following format and provide no other text:\n{format_instructions}
        """),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions(), my_stance=my_stance, topic=topic)

tools = [search_tool, wiki_tool]

# Create agent
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)


agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

chat_history = []

if your_stance.lower() == "for":
    initial_query = input("What is your argument for the topic of the debate? ")
else:
    initial_query = "What is your argument for the topic of the debate?"

raw_response = agent_executor.invoke({"query": initial_query, "chat_history": chat_history})
chat_history.append({"role": "user", "content": initial_query})

structured_response = parser.parse(raw_response.get("output"))
chat_history += f"Bot: {structured_response.my_argument}\n"  # Add bot's response to the history
print("Bot Response: \n", structured_response)


while True:
    query = input(f"User: ")
    
    # print("\n")
    if query.lower() == "exit":
        print("Ending the chat. Thank you!")
        break

    chat_history.append({"role": "user", "content": query})
    
    raw_response = agent_executor.invoke({"query": query, "chat_history": chat_history})

    # print("Raw Response:", raw_response)

    try:
        structured_response = parser.parse(raw_response.get("output"))
        chat_history += f"Bot: {structured_response.my_argument}\n"  # Add bot's response to the history
        print("Bot Response: \n", structured_response)
        
    except Exception as e:
        print("Error parsing response: ", e, "Raw Response: ", raw_response)
        print("Please try again.")
        continue
