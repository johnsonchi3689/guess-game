import random
start = input('請決定開始值')
end = input('請決定結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('猜數字: ')
	num = int(num)
	if num == r:
		print('猜中了')
		print('這是您猜的第', count, '次')
		break
	elif num > r:
		print('太大了')
	elif num < r:
		print('太小了')
	print('這是您猜的第', count, '次')