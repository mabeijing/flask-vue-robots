import string
import base64

# 生成ASCII字母的字符串
alphabet = string.ascii_letters

# 每次迭代写入的字符数
chunk_size = len(alphabet)

# # 重复写入直到文件达到指定大小
# with open('200k.txt', 'w') as f:
#     while f.tell() < 200 * 1024:
#         # 写入每次迭代的字符
#         tag = 200 * 1024 - f.tell()
#         chunk = chunk_size if tag > chunk_size else tag
#         f.write(alphabet[:chunk])

# 重复写入直到文件达到指定大小
# with open('output.txt', 'w') as f:
#     while f.tell() < 200 * 1024:
#         # 写入每次迭代的字符
#         tag = 200 * 1024 - f.tell()
#         chunk = chunk_size if tag > chunk_size else tag
#         f.write(alphabet[:chunk])
#
# with open("output.txt", 'r', encoding='utf-8') as f:
#     d = f.read()
# k_b64 = base64.b64encode(open("output.txt", 'rb').read())
#
# with open("200k_b64.txt", "w", encoding="utf-8") as f:
#     f.write(k_b64.decode())


def file_generate():
    with open("output.txt", "r", encoding="utf-8") as f:
        while True:
         yield f.read(52)

with open("200k_b64_same.txt", 'w', encoding='utf-8') as f:
    gem = file_generate()

    length = 0
    source = ''

    while True:
        txt = next(gem)
        b = base64.b64encode(source.encode())
        if len(b) <= 200*1024:
            source += txt
            continue

        for i in range(len(txt)):
            tmp = source + txt[0:i]
            b = base64.b64encode(tmp.encode())
            if len(b) < 200*1024:
                continue

        break
    f.write(b.decode())









