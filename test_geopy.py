from geopy.distance import geodesic

# 학원의 위도/경도를 tuple로 만들기
coord_nepplus = ( 37.57793434149786, 127.03360495278665)   # 여러개의 값을 넣으면 tuple 형태로 만들어짐 tuple : 내용 변경 불가능한 list

# 집의 위도/경도
coord_home = (37.57832400883555, 127.08126624229462)

print( geodesic(coord_nepplus, coord_home).km)