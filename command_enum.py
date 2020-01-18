from enum import Enum


class Command(Enum):
    """ приветствие """
    hello = ["Привет", "привет", "Ghbdtn", "ghbdtn", "Hi", "hi", "Рш", "рш"]

    """ fb """
    facebook = ["facebook", "пост в фейсбук"]

    """ vk """
    vk = ["vk", "пост в вконтакте"]

    """ показать последние """
    last = ["last", "показать последние"]

    """ пост на стену """
    wall = ["wall", "пост на стену"]

    """ пост в группу """
    group = ["group", "пост в группу"]

    """ назад """
    back = ["back", "назад"]
