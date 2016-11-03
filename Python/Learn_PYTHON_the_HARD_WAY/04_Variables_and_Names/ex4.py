# -*- coding: utf-8 -*-

# 1. 4.0이 아니라 4를 쓰게 된다면 내림으로 계산이 되어서 실제 사람 수 보다 적게
# 측정된다.
cars = 100 # 차량 개수
space_in_a_car = 4.0 # 한 대에 태울 수 있는 사람 수
drivers = 30 # 운전자 수
passengers = 90 # 타려는 승객 수
cars_not_driven = cars - drivers # 운전되지 않는 차량 수
cars_driven = drivers # 운전되는 차량 수
carpool_capacity = cars_driven * space_in_a_car # 운전되는 차량 수 * 태울 수 있는 사람 수
average_passengers_per_car = passengers / cars_driven # 한 대당 타야하는 사람 수


print "자동차", cars, "대가 있습니다."
print "운전자는", drivers, "명 뿐입니다."
print "오늘은 빈 차가", cars_not_driven, "대일 것입니다."
print "오늘은", carpool_capacity, "명을 태울 수 있습니다."
print "함께 탈 사람은", passengers, "명 있습니다."
print "차마다", average_passengers_per_car, "명 정도씩 타야 합니다."

