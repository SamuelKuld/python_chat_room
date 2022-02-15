import time
import traceback


class chat():
    def __init__(self, chat="NO_CHAT_PASSED"):
        if type(str(chat)) == type(str()):
            self.chat = chat
            self.chat_creation_time = time.time()
        else:
            self.chat = "NO_CHAT_PASSED"

    def __repr__(self):
        return self.chat


def test_chat():
    empty_chat_test = chat().chat
    filled_chat_test = chat("test").chat

    print(f"empty_chat_test: {empty_chat_test} : NO_CHAT PASSED")
    print(f"filled_chat_test: {filled_chat_test} : test")


if __name__ == "__main__":
    test_chat()
