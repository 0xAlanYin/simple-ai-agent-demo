#deepseek版本
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
api_key=os.getenv('OPENAI_API_KEY'), # 从环境变量加载API密钥
base_url="https://api.deepseek.com")
)

agent = Agent(model,
             system_prompt='you are an experienced software engineer, you can use the tools to help you to complete the task',
             tools=[tools.read_file,tools.list_files,tools.rename_file]
)

def main():
    # 记录历史的对话
    history = []
    while True:
        user_input = input("input:")
        response = agent.run_sync(user_input, message_history=history)
        history = list(response.all_messages())
        print(response.output)

if __name__ == "__main__":
    main()