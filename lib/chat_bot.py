"""
このファイルは最もシンプルなチャットボットを実装するためのものです。
"""

# チャットボットの基底クラスをインポート
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# チャットボットのクラスを定義
class SimpleChatBot:
    """
    最もシンプルなチャットボットのクラスです。

    :ivar chat: チャットのインスタンス(str)
    :ivar system_message: システムメッセージ(str)
    """

    def __init__(self, temperature=0.7, system_message=""):
        """
        コンストラクタです。

        :param temperature: 温度, defaults to 0.7
        :type temperature: float, optional
        :param system_message: システムメッセージ, defaults to ""
        :type system_message: str, optional
        """
        self.chat = chat=ChatOpenAI(temperature=temperature)
        self.system_message = SystemMessage(content=system_message)

    def talk(self, human_message):
        """
        チャットボットのインスタンスを関数として呼び出すと、
        チャットボットが返すメッセージを返します。

        :param human_message: 人間のメッセージ
        :type human_message: str
        :return: チャットボットが返すメッセージ
        :rtype: str
        """
        return self.chat([self.system_message, HumanMessage(content=human_message)]).content