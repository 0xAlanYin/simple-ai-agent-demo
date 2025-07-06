from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import tools
from dotenv import load_dotenv
import os

load_dotenv()

model = OpenAIModel(
    "deepseek-chat",
    provider=OpenAIProvider(
        api_key=os.getenv('OPENAI_API_KEY'),
        base_url="https://api.deepseek.com"
    )
)

agent = Agent(
    model,
    system_prompt='你是一个经验丰富的软件工程师，可以用工具帮助完成任务',
    tools=[tools.get_host_info]
)

def main():
    history = []
    while True:
        user_input = input("请输入：")
        response = agent.run_sync(user_input, message_history=history)
        history = list(response.all_messages())
        print(response.output)

if __name__ == "__main__":
    main()