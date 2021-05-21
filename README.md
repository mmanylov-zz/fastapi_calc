# Простое приложение для тестирования знания FastAPI и Vue
Приложение имеет один ендпоинт для сложения чисел, суммирующее 2 неотрицательных целых числа: одно из них 
положительное целое число, а другое - неотрицательое целое число. 

Приложение состоит из [frontend](https://github.com/mmanylov/calc_vue) и backend частей.

```sh
curl --location --request POST 'http://127.0.0.1:8000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "x": 1,
    "y": 0
}'
```