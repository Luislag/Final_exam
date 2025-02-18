def is_valid_url(url):
    # Check that the URL starts with a valid protocol.
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    if url.startswith("http://"):
        rest = url[7:]
    else:
        rest = url[8:]
    if not rest.startswith("www."):
        return False
    rest = rest[4:]
    if '.' not in rest:
        return False
    if ' ' in url:
        return False
    parts = rest.split('.')
    for part in parts:
        if part == "":
            return False
    return True
print(is_valid_url("https://www.ie.eu"))
print(is_valid_url("ftp://ie.eu"))
print(is_valid_url("http://ie.eu"))
