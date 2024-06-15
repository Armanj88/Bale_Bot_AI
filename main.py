import asyncio

from handlers import *


async def main():
    bot_info = await bot.get_me()
    print(f"Bot Name: {bot_info.first_name}\tBot Username: @{bot_info.username}\tBot User ID: {bot_info.id}")
    logging.info("Bot Started.")
    logging.info(f"Bot Name: {bot_info.first_name}\tBot Username: @{bot_info.username}\tBot User ID: {bot_info.id}")
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
