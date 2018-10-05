from django.shortcuts import render_to_response

def menu(response):
	food1 = {'name':'滷肉飯',
			'price':35,
			'comment':'在地的美食',
			'spicy':False}
	food2 = {'name':'滑蛋雞肉飯',
			'price':85,
			'comment':'好香',
			'spicy':False}
	food3 = {'name':'麻婆豆腐',
			'price':85,
			'comment':'好辣',
			'spicy':True}
	foods=[food1,food2,food3]
	return render_to_response('menu.html',locals())