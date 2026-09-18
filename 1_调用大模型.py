import os

from openai import OpenAI

# 1.创建客户端对象
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2.调用模型
completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ]
)

# 3.打印输出
print(completion.model_dump_json())
