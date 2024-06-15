import requests
import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class AI:
    def __init__(self):
        self.hajiapi_license = os.getenv("HAJIAPI_LICENSE")
        self.chatgpt_api = "https://api3.haji-api.ir/majid/gpt/3/free?q=%s&license=%s"
        self.llama3_api = "https://api3.haji-api.ir/majid/llama3?p=%s&license=%s"
        self.chat_history_lamma3 = ""
        self.chat_history_chatgpt = ""

    def get_chatgpt(self, message: str) -> str | None:
        self.chat_history_chatgpt += f"Me: {message}\n"
        message = f"Chat History:\n{self.chat_history_chatgpt}\nYou: ?"

        r = requests.get(self.chatgpt_api % (message, self.hajiapi_license))
        if r.status_code == 200:
            response = json.loads(r.text)
            result = response["result"]
            self.chat_history_chatgpt += f"You: {result}\n"
            return result

        return None

    def get_llama3(self, message: str) -> str | None:
        self.chat_history_lamma3 += f"Me: {message}\n"
        message = f"Chat History:\n{self.chat_history_lamma3}\nYou: ?"

        r = requests.get(self.llama3_api % (message, self.hajiapi_license))
        if r.status_code == 200:
            response = json.loads(r.text)
            result = response["result"]
            self.chat_history_lamma3 += f"You: {result}\n"
            return result

        return None
