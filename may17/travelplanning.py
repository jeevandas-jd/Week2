

# travel planning AI agent
# roundrobin group chat way
# this program is more of like 1>2>3>4>5 and then again 1>2>3>4>5 until a certain keyword or term is setuped as a signal for termination.


import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def main():


    # Create the model client
    model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key="AIzaSyCojNDEiD2Lhphj_9vRKbSRItedf-PUQ7o",
    )



    planner_agent = AssistantAgent(
        "planner_agent",
        model_client=model_client,
        description="A helpful assistant that can plan trips.",
        system_message="You are a helpful assistant that can suggest a travel plan for a user based on their request.",
    )

    local_agent = AssistantAgent(
        "local_agent",
        model_client=model_client,
        description="A local assistant that can suggest local activities or places to visit.",
        system_message="You are a helpful assistant that can suggest authentic and interesting local activities or places to visit for a user and can utilize any context information provided.",
    )

    language_agent = AssistantAgent(
        "language_agent",
        model_client=model_client,
        description="A helpful assistant that can provide language tips for a given destination.",
        system_message="You are a helpful assistant that can review travel plans, providing feedback on important/critical tips about how best to address language or communication challenges for the given destination. If the plan already includes language tips, you can mention that the plan is satisfactory, with rationale.",
    )

    travel_summary_agent = AssistantAgent(
        "travel_summary_agent",
        model_client=model_client,
        description="A helpful assistant that can summarize the travel plan.",
        system_message="You are a helpful assistant that can take in all of the suggestions and advice from the other agents and provide a detailed final travel plan. You must ensure that the final plan is integrated and complete. YOUR FINAL RESPONSE MUST BE THE COMPLETE PLAN. When the plan is complete and all perspectives are integrated, you can respond with TERMINATE.",
    )





    termination = TextMentionTermination("TERMINATE")
    group_chat = RoundRobinGroupChat(
        [planner_agent, local_agent, language_agent, travel_summary_agent], termination_condition=termination
    )
    await Console(group_chat.run_stream(task="Plan a 3 day trip to China."))

    await model_client.close()



# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
