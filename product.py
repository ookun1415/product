product = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price) #7到9可以改成 p = [name, price]
	product.append(p) #7到10可以改成product.append([name, price])
print(product)

product[0][0] #product清單第0格的第0格

for a in product:
	print(p[1], '的價格')