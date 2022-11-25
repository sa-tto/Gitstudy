# 1. 2개의 리스트를 선언하여 같은 값을 찾는 프로그램을 작성하시오.

#조건1 : 하나의 리스트는 같은 값을 가져서는 않된다.
#조건2 : 동일한 값 한개만 찾을 수 있도록 한다.
#


#실행예시)

#리스트(1)에 저장된 값 : 5 6 9 1 4
#리스트(2)에 저장된 값 : 7 8 6 2 3

#두 리스트의 동일한 값은 : 6 입니다.

a=[5,6,9,4,1]
b=[7,8,6,2,3]

D = [i for i in a if i in b]



#2. 기존에 수업시간에 실습하였던 자판기 프로그램을 함수로 모듈화 하여 구현하시오.

#조건1
#(1) 동전 투입 함수
#(2) 제품 출력 함수
#(3) 제품 선택 후 금액이 차감되는 함수
#(4) 최종적으로 제품을 구매한 갯수를 출력하는 함수

#조건2 : 동전을 투입할때 2000원 이상은 투입되지 않게 변경



print('리스트(1)에 저장된 값 :',a)

print('리스트(2)에 저장된 값 :',b)
print('두 리스트의 동일한 값은 :',D,'입니다')

my_money = 0
item_menu = 0
item = '아이템'
repeat = 0


def asd():
 my_money = int(input('투입할 금액을 입력해주세요'))
 if my_money >= 2000:
  print('금액이 너무 큽니다.')
 else:
  print(my_money,'원을 투입하셨습니다')
  asd1()
  asd2(my_money)

def asd1():
 print('원하시는 음료의 번호를 입력해 주세요\n1.커피 :200원\n2.우유 :300원\n3.오랜지주스 :600원\n4.바나나우유 :700원')

 
def asd2(my_money):
 item_menu=int(input("제품 선택 : "))
 item_num=int(input("구매할 갯수 :"))
 
 coffie = 200
 milk = 300
 orange = 600
 banana = 700

 if item_menu == 1 :
  end = coffie
  item = '커피'
 if item_menu == 2 :
  end = milk
  item = '우유'
 if item_menu == 3 :
  end = orange
  item = '오렌지주스'
 if item_menu == 4 :
  end = banana
  item = '바나나우유'

 repeat = 0
 while my_money:
  repeat = repeat + 1
  my_money = my_money - end
  if(repeat == item_num or my_money < end):
   asd3(item, repeat, my_money)
   break


def asd3(item, repeat, my_money):
 print(item, "을(를) ", repeat, "개 구매했습니다. 남은 잔액은 ", my_money, "입니다.")


asd()
print('종료')
print('종료')
print('종료')





#3. 지역변수와 전역변수의 차이점을 구별하여 조사해오기
#지역변수는 함수내에서만 사용가는한변수
#전역변수는 어디서든 사용가능한 변수
#지역변수에 return 혹은 global을사용하면 전역변수로 사용가능
