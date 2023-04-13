import json
import base64
import string
import random


def string_same_b64(s: str) -> str:
    length: int = len(s)

    middleIndexArray: list[int] = []

    stopIndex = length

    cursor = 0

    while True:
        sub: str = s[:stopIndex]
        b64_s: str = base64.b64encode(sub.encode()).decode()
        if len(b64_s) == length:
            return b64_s

        if len(b64_s) > length:
            middleIndex = int((cursor + length) / 2)    # 75, 100, 85
            if middleIndex in middleIndexArray:
                return base64.b64encode(s[:cursor].encode()).decode()
            middleIndexArray.append(middleIndex)
            stopIndex = middleIndex  # [0:85]
            cursor = middleIndex  # 85

        else:
            middleIndex = int((stopIndex + length) / 2)  # 85, 100,
            if middleIndex in middleIndexArray:
                return base64.b64encode(s[:cursor].encode()).decode()
            middleIndexArray.append(middleIndex)
            stopIndex = middleIndex  # 75
            cursor = middleIndex  # 75



# string_letters = string.ascii_letters + string.digits + string.punctuation
string_letters = string.ascii_letters + string.digits

generate_str = lambda x: ''.join(random.choices(string_letters, k=x))


def generate_request_body(key_number: int, value: str, b64_encoding: bool = False, keep_size: bool = False):
    request_body: list[dict] = []
    if b64_encoding:
        if keep_size:
            source = string_same_b64(value)
        else:
            source = base64.b64encode(value.encode()).decode()
    else:
        source = value
    for key in range(key_number):
        request_body.append({
            "key": f"STRING.key.{100 + key}",
            "source": source,
            "commentForSource": "",
            "sourceFormat": ""
        })

    return json.dumps(request_body, sort_keys=True)


def for_key_value(file_name: str, value_size: int = 1024):
    # 原始value
    source_value = generate_str(value_size)
    with open(f"{file_name}.txt", mode='w+', encoding="utf-8") as f:
        f.write(source_value)
    print('done')
    # base64
    body = base64.b64encode(source_value.encode()).decode()
    with open(f"{file_name}_b64.txt", mode='w+', encoding="utf-8") as f:
        f.write(body)
    print('done')
    # base64和原始value一样大
    body = string_same_b64(source_value)
    with open(f"{file_name}_b64_same.txt", mode='w+', encoding="utf-8") as f:
        f.write(body)


def for_key_value_array(file_name: str, key_number: int = 10, value_size: int = 1024):
    # 原始value
    source_value: str = generate_str(value_size - 85)

    # key个数 * value大小 = body大小
    body = generate_request_body(key_number, source_value)
    print(len(body))
    with open(f"{file_name}_normal.txt", mode="w+", encoding="utf-8") as f:
        f.write(body)

    # 将body转化成base64。body会变大
    body = generate_request_body(key_number, source_value, b64_encoding=True)
    with open(f"{file_name}_b64.txt", mode="w+", encoding="utf-8") as f:
        f.write(body)

    # body差不多大，内容是base64的
    body = generate_request_body(key_number, source_value, b64_encoding=True, keep_size=True)
    with open(f"{file_name}_b64_same_with_normal.txt", mode="w+", encoding="utf-8") as f:
        f.write(body)


if __name__ == '__main__':
    # 单独的string 200K， 800K , 2M, 5M, 10M
    for_key_value('10m', value_size=1024 * 1024 * 10)
    # for_key_value_array("10m", key_number=100, value_size=1024 * 10 * 10)
