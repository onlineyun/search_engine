import hashlib


def get_md5(url):
    """
    对url进行md5转化，保存起来比较方便（长度等长）
    :param url:
    :return:
    """
    if isinstance(url, str):
        url = url.encode('utf-8')

    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def remove_t_r_n(content):
    """
    去除\t,\r,\n等字符
    :param content:
    :return:
    """
    return content.replace('\t', '').replace('\r', '').replace('\n', '').strip()


if __name__ == '__main__':
    print(get_md5('https://jobbole.com'.encode('utf-8')))

