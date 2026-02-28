import re

email_regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

def is_email_valid(email):
    return bool(re.fullmatch(email_regex, email))

