from requests import get, post, delete, put

print(get('http://localhost:5000/api/v2/users').json(), 3 * '\n')  # Получение всех пользователей
print(get('http://localhost:5000/api/v2/users/2').json(), 3 * '\n')  # Корректное получение одной пользователей
print(get('http://localhost:5000/api/v2/users/999999').json(), 3 * '\n')  # Ошибочный запрос на получение одной пользователей — неверный id
# print(get('http://localhost:5000/api/v2/users/q').json(), 3 * '\n')  # Ошибочный запрос на получение одной пользователей — строка


print(post('http://localhost:5000/api/v2/users', json={}).json(), 3 * '\n')  # Пустой json
print(post('http://localhost:5000/api/v2/users', json={'name': '123'}).json(), 3 * '\n')  # Не все данные в json
print(post('http://localhost:5000/api/v2/users', json={
                                                    'name': 'mark rober',
                                                    'about': 'test',
                                                    'email': 'test@test.com',
                                                    'password': '123'
                                                }).json(), 3 * '\n')  # правильный запрос
print(get('http://localhost:5000/api/v2/users').json(), 3 * '\n')  # Получение всех пользователей

# print(delete('http://localhost:5000/api/v2/users/q').json(), 3 * '\n')  # Не корректный id
print(delete('http://localhost:5000/api/v2/users/999999999').json(), 3 * '\n')  # Не корректный id
print(delete('http://localhost:5000/api/v2/users/4').json(), 3 * '\n')  # правильный запрос
print(get('http://localhost:5000/api/v2/users').json(), 3 * '\n')  # Получение всех пользователей

print(put('http://localhost:5000/api/v2/users', json={'name': 'test2123123123213'}).json(), 3 * '\n')  # нет id в запросе
print(put('http://localhost:5000/api/v2/users/4', json={'name': 'test2123123123213'}).json(), 3 * '\n')  # правильный запрос

print(get('http://localhost:5000/api/v2/users').json(), 3 * '\n')  # Получение всех пользователей