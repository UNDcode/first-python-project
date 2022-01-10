class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

chicken = 10 # 남은 치킨 수
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작  

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order<=0:
            raise ValueError     
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1 # 대기번호 증가
            chicken -= order # 주문 수 만큼 남은 치킨 감소
        if chicken==0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
            
    
            
    except ValueError:
        print("잘못된값을 입력하였습니다.")
        
    except SoldOutError as err:
        print(err)
        break
    

