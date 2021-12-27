class Dog():
    # 각 객체의 변수를 클래스단에 적지 않는다.
    # 함수 / 생성자의 객체에서 달아준다.
    def __init__(self, name, birth_year, type):
        self.name = name
        self.birth_year = birth_year
        self.type = type
        
    # 메쏘드 예시
    # 메쏘드는 어떤 객체가 수행하는 지(self) 반드시 아는 상태로 코드를 작성해야함
    def print_dog_info(self):
        print(f'강아지 이름 : {self.name}')