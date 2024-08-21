from random import randint, shuffle

from dotenv import dotenv_values, set_key

config = dotenv_values()


def shuffle_string(s: str) -> str:
    char_list = list(s)
    shuffle(char_list)
    return ''.join(char_list)


def generate(data_string: str, len_str: int) -> str:
    generated_string: str = ""

    for i in range(len_str):
        index = randint(0, len(data_string) - 1)
        generated_string += data_string[index]

    return generated_string


if __name__ == "__main__":
    string = generate(
        data_string=config["STRING"],
        len_str=32
    )
    string2 = shuffle_string(s=config["STRING"])

    set_key("./.env", "SECRET_CODE", string, quote_mode='always', export=False, encoding='utf-8')
    set_key("./.env", "STRING", string2, quote_mode="always", export=False, encoding="utf-8")