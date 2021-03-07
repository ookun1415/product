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
	print(p[0], '的價格是', p[1], '的價格')

with open('product.csv', 'w', encoding='utf-8') as f: #打開product.csv檔案(csv檔可以用excel打開)(沒有沒關係)，當作f 'w':寫入模式
	f.write('商品,價格\n') #encoding:編碼用來解決亂碼問題  而excel
	for d in product:
		f.write(d[0] + ',' + d[1] + '\n') #利用加把字串和在一起 \n:換行
# write裡面只能有字串