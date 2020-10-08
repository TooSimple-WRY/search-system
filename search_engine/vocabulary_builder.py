passage = []
def get_filename(text):
    with open(text, encoding='utf-8') as fread:
        for line in fread:
            line = line.strip()  # 去掉两端的空白字符，如空格、回车等
            passage.append(line)
    fread.close()
    return passage
