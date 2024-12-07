# Initialise imports
from langchain.agents import AgentExecutor
from langchain import hub
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from composio_langchain import ComposioToolSet, App
from dotenv import load_dotenv
load_dotenv()

user_id = "chrisyooak@gmail.com"
app_name = "gmail"
auth_scheme = "OAUTH2"
toolset = ComposioToolSet()

# connection_request = toolset.initiate_connection(
#     app=app_name,
#     redirect_url = 'https://127.0.0.1:5173/',
#     entity_id=user_id,
#     auth_scheme=auth_scheme,
# )

# print(connection_request.connectedAccountId,connection_request.connectionStatus)
# print(connection_request.redirectUrl)

# toolset = ComposioToolSet()

# # Validate the connection is active
# connected_account = toolset.get_connected_account(id=connection_request.connectedAccountId)
# connection_request.wait_until_active(toolset.client,timeout=60)

tools = toolset.get_tools(apps=[App.GMAIL])

llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0.2)
task = "What are my unread emails?"

agent = create_react_agent(llm, tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute using agent_executor
inputs = {"messages": [("user",  task)]}
agent_executor.invoke(input=inputs)
