import re

name = ""

def normalize(name):

    upper_albet = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Є': 'Ie',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'Y',
        'І': 'I',
        'Ї': 'Ii',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'Kh',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ь': '',
        'Ю': 'Iu',
        'Я': 'Ia',
        "Ё": '_',
        "Ы": '_',
        "Ъ": '_',
        "Э": '_'
    }

    lower_albet = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'є': 'ie',
        'ж': 'zh',
        'з': 'z',
        'и': 'y',
        'і': 'i',
        'ї': 'ii',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'kh',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ь': '',
        'ю': 'iu',
        'я': 'ia',
        "ё": '_',
        "ы": '_',
        "ъ": '_',
        "э": '_'
    }

    for k, v in upper_albet.items():
        name = name.replace(k, v)

    for k, v in lower_albet.items():
        name = name.replace(k, v)

    for char in name:
        if not re.search('[a-zA-Z0-9._]', char):
            name = name.replace(char, "_")

    return name


normalize(name)
