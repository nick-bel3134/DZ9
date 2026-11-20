import requests

res_parse_list = []
res_parse_list2 = []

response = requests.get("https://books.toscrape.com")
response.raise_for_status()

response_text = response.text
response_parse = response_text.split('title="')

for parse_elem_1 in response_parse[1:]:
    title = parse_elem_1.split('"')[0]
    if title:
        res_parse_list.append(title)

response_parse2 = response_text.split('<p class="price_color">')

for parse_elem_3 in response_parse2[1:]:
    price = parse_elem_3.split("</p>")[0]
    price = price.replace("Â", "").strip()

    if price:
        res_parse_list2.append(price)

print(res_parse_list)
print(res_parse_list2)