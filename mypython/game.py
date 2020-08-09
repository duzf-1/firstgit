import random
secret = random.randint(1,10)
print("---这是我的python小程序---")
temp = input('不妨猜一下我的幸运数字，来吧！')
guess = int(temp)
while guess != secret:
	temp = input("哎呦，错了哦，再来一次吧：")
	guess = int(temp)
	if guess == secret:
		print('哇，你真厉害，居然猜中了！')
		print("哼，那又怎样，反正没奖品，哈哈哈！")
	else:
		if guess < secret:
			print('不对啦，再大点嘛！')
		else:
			print("呀，有点大了耶！")
print('累了，歇会吧，游戏结束！')

