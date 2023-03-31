# チャットを行う実行プログラム
import sys
from termcolor import colored
from chat_bot import SimpleChatBot
from text_to_speech import text_to_siri_async, text_to_voicevox_async

# チャットの実行
if __name__ == '__main__':
    simple_chat_bot = SimpleChatBot(system_message="優しくしてね")

    while True:
        print("")
        user_input = input("あなた: ")
        print("")

        if user_input.lower() in ["終了", "exit"]:
            break

        sys.stdout.write(colored("Accessing...", "blue"))
        sys.stdout.flush()

        ai_message = simple_chat_bot.talk(user_input).content

        sys.stdout.write("\r")  # テキストの先頭に戻る
        sys.stdout.write("            ")  # テキストを消去
        sys.stdout.write("\r")  # テキストの先頭に戻る
        sys.stdout.flush()

        print(colored(f"AI: {ai_message}", "blue"))
        text_to_voicevox_async(ai_message, speaker=47)