from datetime import datetime


def sanitize_str(data):
    if data == '':
        raise ValueError()
    return data.replace('\t', ' ').replace('|', '').strip()


def sanitize_bool(data, default):
    if data == '' and default is not None:
        return default
    if data in ['д', 'Д', 'да', 'Да']:
        return True
    if data in ['н', 'Н', 'нет', 'Нет']:
        return False
    raise ValueError()


def sanitize_date(data):
    parts = data.split('.')
    if len(parts) == 2:
        year = datetime.today().year
        day, month = parts
        return datetime.fromisoformat(f"{year}-{month}-{day}")

    if len(parts) == 3:
        day, month, year = parts
        if len(year) == 2:  # so 01.01.01 == 01.01.2001
            year = str(datetime.today().year)[:2] + year
        return datetime.fromisoformat(f"{year}-{month}-{day}")

    raise ValueError()


def sanitize_int(data):
    val = int(data)
    if val <= 0:
        raise ValueError
    return val

