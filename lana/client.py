
import requests
class LanaClient():
  def __init__(self, host, port):
    self.host = host
    self.port = port

  def create_basket(self):
    try:
      x = requests.post('http://{}:{}/api/v1/basket'.format(self.host, self.port))
    except e:
      print('error: {}'.format(e))
      return None
    if x.status_code != 201:
      # some error ocurred
      return None
    basket = x.json()
    return basket

  def add_to_basket(self, basket_id, product_code, count ):
    try:
      x = requests.post(
        'http://{}:{}/api/v1/basket/{}'.format(self.host, self.port, basket_id),
        json={
          'product': product_code,
          'count': count
        })
    except e:
      print('error: {}'.format(e))
      return None
    if x.status_code != 201 and x.status_code != 200:
      # some error ocurred
      return None
    count = x.json()
    return count['count']

  def get_basket(self, basket_id):
    try:
      x = requests.get(
        'http://{}:{}/api/v1/basket/{}'.format(self.host, self.port, basket_id))
    except e:
      print('error: {}'.format(e))
      return None
    if x.status_code == 404:
      print('Basket not found')
      return None
    if x.status_code != 200:
      # some error ocurred
      return None
    return x.json()

  def delete_basket(self, basket_id):
    try:
      x = requests.delete(
        'http://{}:{}/api/v1/basket/{}'.format(self.host, self.port, basket_id))
    except e:
      print('error: {}'.format(e))
      return None
    if x.status_code == 404:
      print('Basket not found')
      return None
    if x.status_code != 204:
      # some error ocurred
      return None
    return True

  def get_all_baskets(self):
    try:
      x = requests.get(
        'http://{}:{}/api/v1/basket/'.format(self.host, self.port))
    except e:
      print('error: {}'.format(e))
      return None
    if x.status_code != 200:
      # some error ocurred
      return None
    return x.json()