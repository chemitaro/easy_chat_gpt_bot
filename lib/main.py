# チャットを行う実行プログラム

from chat_bot import SimpleChatBot
from termcolor import colored
from text_to_speech import text_to_siri_async, text_to_voicevox_async

# チャットの実行
if __name__ == '__main__':
    simple_chat_bot = SimpleChatBot(system_message="優しくしてね")

    while True:
        print("")
        user_input = input("あなた: ")

        if user_input.lower() in ["終了", "exit"]:
            break

        ai_message = simple_chat_bot.talk(user_input).content
        print("")
        print(colored(f"AI: {ai_message}", "magenta"))
        text_to_voicevox_async(ai_message, speaker=19)