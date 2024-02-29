help_prompt = """
/help | Send you this message
"""


def check_nickname_input(nickname):
    MAX_LEN = 16
    MIN_LEN = 4

    banned_words = []
    with open("BANNED_WORDS_LIST_PATH_HERE.TXT") as f:
        banned_words = f.readlines()
    banned_words = [word.strip() for word in banned_words]

    if nickname in banned_words:
        return "WORD NOT ALLOWED"
    
    if len(nickname) > MAX_LEN:
        return "Nickname to long (16 char max | INCLUDES SPACES)"
    
    if len(nickname) < MIN_LEN:
        return "Nickname to short (4 char min)"
    
    if not nickname.isalpha():
        return "Nickname can't be anything besides letters"

    return True
