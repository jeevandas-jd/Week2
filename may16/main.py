import autogen

#import openai
#google api "AIzaSyC0IeKjfDwI8KyyLgEwwH5rSE2NuApZnVI"
"""  
      {
        "model": "gemini-pro",
        "api_key": "AIzaSyABBfec3SXrG-_yMsjexuoB-zAFRoOiUT8",
        "api_type": "google"

    } 
             {
        "model":"gpt-35-turbo",
        "api_key":"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"
    },
     ,"""
try:
    config_list=[
        {

               "model": "gemini-1.5-flash",
        "api_key": "AIzaSyABBfec3SXrG-_yMsjexuoB-zAFRoOiUT8",
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