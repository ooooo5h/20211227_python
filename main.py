from dog import Dog


dog1 = Dog('해피', 2016, '푸들')

dog2 = Dog('바둑', 2014, '믹스견')

dog1 = dog2

dog1.name = '아롱이'

print(f'dog1의 이름 : {dog1.name}')   # 이름이 아롱이
print(f'dog2의 이름 : {dog2.name}')   # 이름이 아롱이
