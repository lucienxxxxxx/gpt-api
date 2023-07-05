import os
import time

import openai

openai.api_key = "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"
CHAT_MODEL = "gpt-3.5-turbo-16k"
COMPLETION_MODEL = "text-davinci-003"


def getModels():
    return openai.Model.list()


def chat(prompt, message):
    """
    用来聊天的，最强大的 GPT-3.5 模型，并针对聊天进行了优化，成本仅为“text-davinci-003”的 1/10。将在发布后两周更新我们最新的模型迭代。
    :param prompt:
    :param message:
    :return:
    """
    resp = openai.ChatCompletion.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ]
    )
    print(resp.choices[0].message)
    return resp.choices[0].message.content


def completion(prompt):
    """
    用来完成任务的
    Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.
    :param prompt:
    :return:
    """
    resp = openai.Completion.create(
        model=COMPLETION_MODEL,
        prompt=prompt,
        temperature=0
    )
    print(resp.choices[0].text)
    return resp.choices[0].text


def chat_stream(prompt, message):
    # Example of an OpenAI ChatCompletion request with stream=True
    # https://platform.openai.com/docs/guides/chat

    # record the time before the request is sent
    start_time = time.time()

    # send a ChatCompletion request to count to 100
    response = openai.ChatCompletion.create(
        model=CHAT_MODEL,
        messages=[
            {'role': 'user',
             'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
        ],
        temperature=0,
        stream=True  # again, we set stream=True
    )

    # create variables to collect the stream of chunks
    collected_chunks = []
    collected_messages = []
    # iterate through the stream of events
    for chunk in response:
        chunk_time = time.time() - start_time  # calculate the time delay of the chunk
        collected_chunks.append(chunk)  # save the event response
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        collected_messages.append(chunk_message)  # save the message
        print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

    # print the time delay and text received
    print(f"Full response received {chunk_time:.2f} seconds after request")
    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    print(f"Full conversation received: {full_reply_content}")
