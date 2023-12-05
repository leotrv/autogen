from autogen import AssistantAgent, UserProxyAgent

config_list = [
    {
        "model": "llama2-7B-gguf",
        "api_base": "http://172.20.64.1:1234/v1", # accessing Win11 localhost from WSL2
        "api_type": "open_ai",
        "api_key": "None",
        "request_timeout": 1000
    }
]
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(name="user_proxy", default_auto_reply= "This sounds great!", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")