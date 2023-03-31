# チャットを行う実行プログラム
import sys
from termcolor import colored
from chat_bot import SimpleChatBot
from chat_bot_memory import MemoryChatBot
from text_to_speech import text_to_siri_async, text_to_voicevox_async

# チャットの実行
if __name__ == '__main__':
    chat_bot = MemoryChatBot(system_message="優しくしてね")

    while True:
        print("\nuser: ")
        user_input = sys.stdin.read()
        print("")

        if user_input.lower() in ["終了\n", "exit\n"]:
            break

        sys.stdout.write(colored("Accessing...", "blue"))
        sys.stdout.flush()

        ai_message = chat_bot.talk(user_input)

        sys.stdout.write("\r")  # テキストの先頭に戻る
        sys.stdout.write("            ")  # テキストを消去
        sys.stdout.write("\r")  # テキストの先頭に戻る
        sys.stdout.flush()

        print(colored("\nassistant:", "blue"))
        print(colored(f"{ai_message}", "blue"))
        text_to_voicevox_async(ai_message, speaker=47)