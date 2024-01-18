class Message:
    fl_like = False

    def __init__(self, text: str) -> None:
        self.text = text


class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg: Message):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.messages.remove(msg)

    @classmethod
    def set_like(cls, msg: Message):
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, indx: int):
        print(cls.messages[indx:])

    @classmethod
    def total_messages(cls):
        return len(cls.messages)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
