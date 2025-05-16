import autogen
from dotenv import load_dotenv
import os
load_dotenv()
try:
    config_list=[
        {

        "model": "gemini-1.5-flash",
        "api_key": os.getenv("api_key"),
        "api_type": "google"

    } 
    ]
    llm_config={
    
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
    }
    asisstent=autogen.AssistantAgent(
    name="CEO",
    llm_config=llm_config
    )
    userProxy=autogen.UserProxyAgent(
    name="userProxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir":"web","use_docker":False},
    llm_config=llm_config
    )

    task="""write a function to get odd number from a given list of integers"""

    userProxy.initiate_chat(asisstent,message=task)
except Exception as e:
    print(f"Error occured:\n{e}")