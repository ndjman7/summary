# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 188 # cm
weight = 82 # kg
eyes = '파랑'
teeth = '하양'
hair = '갈색'
inch_height = height / 2.54
pound_weight = weight * 0.4536

print "%s에 대해 이야기해 보죠." % name
print "키는 %d 센티미터고요." % height
print "몸무게는 %d 킬로그램이에요." % weight
print "사실 아주 많이 나가는 건 아니죠."
print "눈은 %s이고 머리는 %s이에요." %(eyes, hair)
print "이는 보통 %s이고 커피를 먹으면 달라져요." % teeth

# 이 줄은 까다롭지만 정확히 따라 하세요
print "%d, %d, %d를 모두 더하면 %d 랍니다." % (
    age, height, weight, age + height + weight)

print "%r Inch, %r Pound." % (round(inch_height), round(pound_weight))
