import autogen

config_list = [
    {
        "model": "gemini-1.5-flash",
        "api_type": "google",
        "api_key": "AIzaSyDl7hvmtuosswT62ty3V-SDmrWXAy3Z-pE"  # Replace with your valid key
    }
]

llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

# Define Assistant Agent
assistant = autogen.AssistantAgent(
    name="CTO",
    llm_config=llm_config,
    system_message="Chief technical officer of a tech company"
)

# Define User Proxy Agent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "response",
        "use_docker": False  # 👈 This disables docker
    },
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

# Task 1: Write code to output numbers 1 to 100
task = """
Write Python code to output numbers 1 to 100, and then store the code in a file
"""
user_proxy.initiate_chat(
    assistant,
    message=task
)

# Task 2: Modify code to output numbers 1 to 200
task2 = """
Change the code in the file you just created to instead output numbers 1 to 200
"""
user_proxy.initiate_chat(
    assistant,
    message=task2
)