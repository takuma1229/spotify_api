import requests
from xml.etree import ElementTree
url = 'https://ext.nicovideo.jp/api/getthumbinfo/sm39777009'
response = requests.get(url)
tree = ElementTree.fromstring(response.content)
response = requests.get(url, stream=True)
response.raw.decode_content = True
events = ElementTree.iterparse(response.raw)

print(tree)
# for event, elem in events:
#     print('タグ:', elem.tag, elem.attrib)
#     print('テキスト:', elem.text)
#     print('-----------------------------\n')
