from aiogram.handlers import ErrorHandler
from aiogram.types import Message

from bot import *
from ai import *


last_message_id = {}
ai = AI()


@dispatcher.errors()
class ErrorHandler(ErrorHandler):
    async def handle(self):
        logging.exception(
            "Cause unexpected exception %s: %s",
            self.exception_name,
            self.exception_message
        )


def check_for_duplicate_message(user_id: int, message_id: int) -> bool:
    if user_id not in last_message_id:
        last_message_id[user_id] = -1
        return False

    if message_id == last_message_id[user_id]:
        return True

    last_message_id[user_id] = message_id

    return False


@dispatcher.message()
async def on_message(message: Message):
    # chat_type = message.chat.type
    user_name = message.chat.first_name
    user_username = message.chat.username
    user_id = message.chat.id
    message_id = message.message_id
    message_text = message.text
    # message_content_type = message.content_type

    if check_for_duplicate_message(user_id, message_id):
        return

    logging.info(
        f"User ID: {user_id}\tName: {user_name}\tUsername: {user_username}\tTime: {message.date.now()}\t"
        f"Message: {message_text}")

    if message.text == "/start":
        await message.answer("Type /help for starting!")
    elif message.text == "/help":
        await message.answer("""Type /help for getting help.
Type /lamma3 {message} for talking to Lamma3.
Type /chatgpt {message} fro talking to ChatGPT 3.
Type /reset to reset the chat history.""")
    elif message.text.startswith("/lamma3 "):
        prompt = message.text[7:].strip()
        response = ai.get_llama3(prompt)
        await message.answer(response)
    elif message.text.startswith("/chatgpt "):
        prompt = message.text[8:].strip()
        response = ai.get_chatgpt(prompt)
        await message.answer(response)
    elif message.text == "/reset":
        ai.chat_history_chatgpt = ""
        ai.chat_history_lamma3 = ""
        await message.answer("Chat History is reset.")
    else:
        await message.answer("I can't understand :( Please type /help for getting help. or try again :)")
