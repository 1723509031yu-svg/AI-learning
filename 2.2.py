from openai import OpenAI

# 1. 创建客户端对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 2. 存储对话历史
chat_history = []

# 3. 第一次调用：向模型告知用户身份
user_message_1 = "你好，我是阿苑，是一个AI老师。"
chat_history.append({"role": "user", "content": user_message_1})

completion = client.chat.completions.create(
    model="qwen3-max",
    messages=chat_history
)
chat_history.append({"role": "assistant", "content": completion.choices[0].message.content})

# 4. 第二次调用：询问模型“我是谁？”
user_message_2 = "我是谁？"
chat_history = chat_history + [{"role": "user", "content": user_message_2}]
# print("记忆内容：", chat_history)
completion = client.chat.completions.create(
    model="qwen3-max",
    messages=chat_history
)

# 5. 输出完整的响应内容
print(completion.model_dump_json())