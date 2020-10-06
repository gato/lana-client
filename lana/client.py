
import requests
class LanaClient():
  def __init__(self, host, port):
    self.baseurl = '{}:{}/api/v1/basket/'.format(host, port)

  def create_basket(self):
    try:
      x = requests.post(self.baseurl)
    except Exception as e:
      return None, 'Exception: {}'.format(e)
    if x.status_code != 201:
      return None, 'Invalid status code {}'.format(x.status_code)
    return x.json(), None

  def get_all_baskets(self):
    try:
      x = requests.get(self.baseurl)
    except Exception as e:
      return None, 'Exception: {}'.format(e)
    if x.status_code != 200:
      return None, 'Invalid status code {}'.format(x.status_code)
    return x.json(), None

  def add_to_basket(self, basket_id, product_code, count ):
    try:
      x = requests.post('{}{}'.format(self.baseurl, basket_id),
        json={'product': product_code,'count': count})
    except Exception as e:
      return None, 'Exception: {}'.format(e)
    if x.status_code != 201 and x.status_code != 200:
      return None, 'Invalid status code {}'.format(x.status_code)
    return x.json()['count'], None

  def get_basket(self, basket_id):
    try:
      x = requests.get('{}{}'.format(self.baseurl, basket_id))
    except Exception as e:
      return None, 'Exception: {}'.format(e)
    if x.status_code == 404:
      return None, 'Basket Not Found'
    if x.status_code != 200:
      return None, 'Invalid status code {}'.format(x.status_code)
    return x.json(), None

  def delete_basket(self, basket_id):
    try:
      x = requests.delete('{}{}'.format(self.baseurl, basket_id))
    except Exception as e:
      return 'Exception: {}'.format(e)
    if x.status_code == 404:
      return 'Basket Not Found'
    if x.status_code != 204:
      return 'Invalid status code {}'.format(x.status_code)
    return None
