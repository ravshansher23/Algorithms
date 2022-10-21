import hashlib


def cash(url, memory={}):
    r = memory.get(url)
    if r is None:
        salt = 'body'
        r = hashlib.sha256(url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        memory[url] = r
        return print(f'Добавлен хэш {r}')
    return print(f'Уже есть хэш {r}')
cash('www.asd.com')
cash('www.asd.com')
