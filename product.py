import os #os(operating system):作業系統模組


product = []
if os.path.isfile('product.csv'): #os模組裡的path模組裡的isfile功能 #檢查同路徑裡有沒有這個檔名
	print('找到檔案')
	with open('product.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #continue:直接跳到下一次迴圈
			name, price = line.strip().split(',')#split:切割  ()裡面:以什麼當切割的標準
			product.append([name, price])
	print(product)
else:
	('找不到檔案')
#讀取檔案

#strip:刪除換行

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	product.append([name, price])
	
print(product)

#印出所有購買紀錄
for p in product:
	print(p[0], '的價格是', p[1])
#寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f: #打開product.csv檔案(csv檔可以用excel打開)(沒有沒關係)，當作f 'w':寫入模式
	f.write('商品,價格\n') #encoding:編碼用來解決亂碼問題  而excel要從取得資料那邊拿到原本的檔案然後改成utf-8
	for d in product:
		f.write(d[0] + ',' + d[1] + '\n') #利用加把字串和在一起 \n:換行
# write裡面只能有字串
