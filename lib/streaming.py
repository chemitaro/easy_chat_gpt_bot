# チャットを行う実行プログラム
import sys
from termcolor import colored
from chat_bot import SimpleChatBot
from chat_bot_memory import MemoryChatBot
from chat_bot_streaming import StreamingChatBot
from text_to_speech import text_to_siri_async, text_to_voicevox_async

# チャットの実行
if __name__ == '__main__':
    chat_bot = StreamingChatBot(system_message="")

    while True:
        print("\n")
        print(colored("user:", "green"))
        user_input = sys.stdin.read()
        print("")

        if user_input.lower() in ["終了\n", "exit\n"]:
            break

        print(colored("\nassistant:", "blue"))
        ai_message = chat_bot.talk(user_input)

        text_to_voicevox_async(ai_message, speaker=47)