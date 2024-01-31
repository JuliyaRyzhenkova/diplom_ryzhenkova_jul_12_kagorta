import configuration
import requests
import data


# создание заказа
def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.POST_CREATE_ORDER,
                         json=order_body)


response = post_create_order(data.order_boby)

# сохранение трека
track_number = response.json()["track"]

print(response.status_code)
print(response.json())


# получение заказа по треку
def get_order_by_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
                        params={"t": track_number})


# response = get_order_by_track_number()
print(response.status_code)
