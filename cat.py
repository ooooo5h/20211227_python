from animal import Animal

class Cat(Animal):
    
    # 동물 -> 고양이 : 출생년도/성별 + 달리기(메쏘드)
    
    # 기능 추가 - 고양이만의 별도 기능
    def play_with_human(self, owner_name):
        print(f'고양이가 {owner_name}과 놀아줍니다.')
        
    # 물려받은 기능 수정 - 고양이가 뛰어다니는 기능
    def run(self):
        # 원래 동물로서 뛰어다니는 기능도 같이 실행하고싶다
        super().run()
        print('고양이가 뛰어다닙니다.')
        
    # # 사람과 놀아주는 기능 추가 작성
    def play_with_human(self):
        print(f'고양이가 사람과 놀아주는 두번째 메쏘드입니다.')