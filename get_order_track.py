import sender_stand_request



def positiv_assert(track_number):
    # переменная включает в себя результат запроса на получение заказа по треку
    order_response = sender_stand_request.get_order_by_track_number(track_number)
    # Проверка, что код ответа 200
    assert order_response.status_code == 200

# Тест
def test_get_order_track():
    positiv_assert(sender_stand_request.track_number)