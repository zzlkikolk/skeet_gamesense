import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 获取标题
    title = soup.title.string if soup.title else 'No title'

    # 获取所有段落
    paragraphs = [p.get_text() for p in soup.find_all('p')]

    return title, paragraphs


def main():
    url = 'https://www.example.com'  # 替换为你想爬取的页面地址
    html_content = fetch_webpage(url)

    if html_content:
        title, paragraphs = parse_html(html_content)
        print(f"Title: {title}")
        for i, p in enumerate(paragraphs, start=1):
            print(f"Paragraph {i}: {p}")


if __name__ == '__main__':
    main()
