from autogen import AssistantAgent, UserProxyAgent

config_list = [
    {
        'model': 'gpt-4-0613',
        'api_key': 'YOUR OPENAI API KEY'
    }
]

llm_config = {'config_list': config_list}

#create an instance of AssistanAgent
assistant = AssistantAgent(
    name = "assistant",
    llm_config=llm_config
)

#create an instance of UserProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
    system_message='A Human input',
    human_input_mode="NEVER"
)

user_proxy.initiate_chat(
    assistant,
    message = """Find the latest paper about gpt-4 on arxiv and find its potential application in software"""
)
