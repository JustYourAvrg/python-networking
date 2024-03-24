# Check the nickname for none, length, server, spaces, and return the result
def nickname_checks(nickname):
    if not nickname:
        return 'NICKNAME CANNOT BE EMPTY'
    
    if len(nickname) > 12:
        return 'NICKNAME CANNOT BE MORE THEN 12 CHARACTERS'

    if len(nickname) < 4:
        return 'NICKNAME CANNOT BE LESS THEN 4 CHARACTERS' 
    
    if nickname.lower() == 'server':
        return 'NICKNAME CANNOT BE SERVER'
    
    if ' ' in nickname.lower():
        return 'NICKNAME CANNOT CONTAIN SPACES'
    
    return True
