from dog import Dog


dog1 = Dog('해피', 2016, '푸들')

dog2 = Dog('바둑', 2014, '믹스견')

dog1 = dog2

dog1.name = '아롱이'

print(f'dog1의 이름 : {dog1.name}')   # 이름이 아롱이
print(f'dog2의 이름 : {dog2.name}')   # 이름이 아롱이

# 함수를 만드는 예시
# 함수 : 특정 객체가 실행하는 코드가 아니라 일반적인 단순 기능을 수행하는 아이들
# 어느 객체가 실행하는지 굳이 알 필요가 없어서 self같은 변수를 파라미터로 만들지 않는다.
def print_main_info():
    print('이 함수는 main.py에서 실행됩니다.')

    # 함수와 메쏘드의 공통점 : 정의하고나서, 사용하는 코드를 추가 작성해야 호출이 됨  
    
# 함수 호출 예시   
# 특징 : 함수() 곧바로 불러낸다
print_main_info()

# 메쏘드 호출 예시
# 특징 : 변수이름"."메쏘드() 형태로 사용함
dog1.print_dog_info()