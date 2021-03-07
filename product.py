#讀取檔案
product = []
with open('product.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #continue:直接跳到下一次迴圈
		name, price = line.strip().split(',')#split:切割  ()裡面:以什麼當切割的標準
		product.append([name, price])
#strip:刪除換行
print(product)

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	product.append([name, price])
	
print(product)


for p in product:
	print(p[0], '的價格是', p[1])

with open('product.csv', 'w', encoding='utf-8') as f: #打開product.csv檔案(csv檔可以用excel打開)(沒有沒關係)，當作f 'w':寫入模式
	f.write('商品,價格\n') #encoding:編碼用來解決亂碼問題  而excel要從取得資料那邊拿到原本的檔案然後改成utf-8
	for d in product:
		f.write(d[0] + ',' + d[1] + '\n') #利用加把字串和在一起 \n:換行
# write裡面只能有字串
