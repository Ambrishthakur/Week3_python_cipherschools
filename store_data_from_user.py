
# user = {
# 'name' : 'Ambrish'
# 'age' : 18,
# 'fav_movies' : ['coco' , 'avengers']
# 'fav_songs' : ['song1' . song2]
# }


#solution

user = {}

name = input('what is your name: ')
age = input('what is your age: ')
fav_movies = input('your fav movies separated by comma  ').split(',')
fav_songs = input('your fav songs separated by comma  ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs


for key, value in user.items():
    print(f"{key} : {value}")
