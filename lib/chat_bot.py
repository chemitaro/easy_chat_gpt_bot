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

# チャットボットのインスタンスを作成
