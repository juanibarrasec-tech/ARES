import re
def valid_domain(d):
    return re.match(r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", d) is not None
