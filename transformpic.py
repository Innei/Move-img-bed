import re
import requests
import os


def parse_links(paths):
    links = []
    r = re.compile(r'!\[.*?\]\((.*?)\)', re.S)
    for path in paths:
        with open('_posts/' + path, 'r', encoding='utf-8') as f:
            s = f.read()
            link = re.findall(r, s)
            for i in link:
                links.append(i)

    # print(links, len(links))
    return links


def download_pic(urls):
    r = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; MX4 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',

    }
    fail_url = []
    try:
        os.mkdir('out')
    except FileExistsError:
        pass
    for url in urls:
        try:
            name = url.split('/')[-1]
            print('处理 ----> ', url)
            with open('out/' + name, 'wb+') as f:
                f.write(r.get(url, headers=headers).content)
        except Exception as e:
            fail_url.append(url)
    print('失败列表: ', fail_url)


if __name__ == '__main__':
    paths = [f for f in os.listdir('_posts') if not f.startswith('.')]

    download_pic(parse_links(paths))
