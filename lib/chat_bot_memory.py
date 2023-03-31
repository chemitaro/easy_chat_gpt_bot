"""
このファイルメモリー機能を持つチャットボットを実装するためのものです。
"""

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

# チャットボットのクラスを定義
class MemoryChatBot:
    """
    最もシンプルなチャットボットのクラスです。

    :ivar conversation: 会話のインスタンス
    :vartype conversation: ConversationChain
    """

    def __init__(self, temperature=0.7, system_message=""):
        """
        コンストラクタです。

        :param temperature: 温度, defaults to 0.7
        :type temperature: float, optional
        :param system_message: システムメッセージ, defaults to ""
        :type system_message: str, optional
        """
        llm = ChatOpenAI(temperature=temperature)
        prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_message),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{input}")
        ])
        memory = ConversationBufferMemory(return_messages=True)

        self.conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

    def talk(self, human_message):
        """
        チャットボットのインスタンスを関数として呼び出すと、
        チャットボットが返すメッセージを返します。

        :param human_message: 人間のメッセージ
        :type human_message: str
        :return: チャットボットが返すメッセージ
        :rtype: str
        """
        return self.conversation.predict(input=human_message)