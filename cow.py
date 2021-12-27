from animal import Animal

class Cow(Animal):
    
    # 소 만의 고유 기능 : work_hard(파라미터 x) -> 소가 열심히 일을 합니다.
    def work_hard(self):
        print('소가 열심히 일을 합니다.')
  
    # 소가 뛰어다니는 기능 => '소가 뛰어다닙니다.' 출력 문구 변경      
    def run(self):
        print('소가 뛰어다닙니다.')