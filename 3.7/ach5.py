import sys
from typing import List


class MailItem:
    def __init__(self, mail_from: str, title: str, content: str) -> None:
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read: bool) -> None:
        self.is_read = fl_read

    def __bool__(self) -> bool:
        return self.is_read


class MailBox:
    def __init__(self) -> None:
        self.inbox_list: List[MailItem] = []

    def __len__(self) -> int:
        return len(self.inbox_list)

    def recieve(self) -> None:
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list = [MailItem(*string.split('; ')) for string in lst_in]


mail = MailBox()
mail.recieve()
mail.inbox_list[0].set_read(True)
mail.inbox_list[len(mail) - 1].set_read(True)
inbox_list_filtered = list(filter(None, mail.inbox_list))
print(inbox_list_filtered)
