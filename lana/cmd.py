#!python3
import readline
from cmd import Cmd
from .client import LanaClient

class LanaCmd(Cmd):
  
  def __init__(self, host, port):
    super(LanaCmd, self).__init__()
    self.host = host
    self.port = port
    self.update_basket(None)

  def update_basket(self, basket):
    self.basket = basket
    if self.basket == None:
      self.prompt = 'no basket > '
      return
    self.prompt = 'basket: {} > '.format(self.basket['id'])

  def error(self, msg):
    print('*** Error: {}\n'.format(msg))

  def parse_count(self, inp):
    if inp == '':
      return 1
    inp = inp.split(' ')
    if len(inp) != 1:
      return None
    try:
      return int(inp[0])
    except ValueError:
      return None

  def add_item(self, product_code, inp):
    if self.basket == None:
      return self.error('No basket selected')
    count = self.parse_count(inp)
    if count == None:
      return self.error('invalid number of {}S'.format(product_code))
    client = LanaClient(self.host, self.port)
    count = client.add_to_basket(self.basket['id'], product_code, count)
    if count == None:
      return self.error('adding {} to basket'.format(product_code))
    print('{} {}S in basket\n'.format(count, product_code))

  def print_basket(self):
    print('')
    if len(self.basket['items']) == 0:
      print('Basket is empty\n')
      return
    print('Basket content:')
    for item in self.basket['items']:
      print('  {:6} {}'.format(item['product'], item['count']))
    print("\nTotal basket cost is {:.2f}\n".format(self.basket['amount']))
      
  def do_new(self, inp):
    '''
creates a new empty basket
    '''        
    self.basket_id = None
    client = LanaClient(self.host, self.port)
    basket = client.create_basket()
    if basket == None:
      return self.error('creating basket')

    self.update_basket(basket)
    print('Basket {} created!\n'.format(self.basket['id']))

  def do_pen(self, inp):
    '''
add PEN to basket
    ''' 
    self.add_item('PEN', inp)

  def do_tshirt(self, inp):
    '''
add TSHIRT to basket
    ''' 
    self.add_item('TSHIRT', inp)

  def do_mug(self, inp):
    '''
add MUG to basket
    ''' 
    self.add_item('MUG', inp)     
  
  def do_use(self, inp):
    '''
select an existing basket
    ''' 
    if inp == '':
      return self.error('missing basket parameter')
    inp = inp.split(' ')
    if len(inp) != 1:
      return self.error('invalid number of paramters')
    client = LanaClient(self.host, self.port)
    basket = client.get_basket(inp[0])
    if basket == None:
      return self.error('error selecting basket. basket not changed')
    self.update_basket(basket)
    print('basket changed to {}\n'.format(self.basket['id']))
    self.print_basket()

  def complete_use(self, text, line, begidx, endidx):
    # TODO I should cache this. but not now
    client = LanaClient(self.host, self.port)
    baskets = client.get_all_baskets()
    if len(text) > 0:
      baskets = list(filter(lambda x: x.startswith(text), baskets))
    return baskets

  def reload_basket(self):
    if self.basket == None:
      return self.error('No basket selected')
    client = LanaClient(self.host, self.port)
    self.update_basket(client.get_basket(self.basket['id']))
    if self.basket == None:
      return self.error('error. basket not found')

  def do_total(self, inp):
    '''
get basket's total cost (with promotions already applied)
    '''      
    self.reload_basket()
    if self.basket == None:
      return
    self.print_basket()

  def do_remove(self, inp):
    '''
delete current basket
    '''
    self.reload_basket()
    if self.basket == None:
      return self.error('error. basket not found')
    print('\n*******')
    print('You are going to remove basket {}'.format(self.basket['id']))
    self.print_basket()
    result = input('\nAre you sure [Y/N]? ')
    if result.lower() != 'y':
        self.error('aborted')
        return
    client = LanaClient(self.host, self.port)
    if client.delete_basket(self.basket['id']) == None:
      return self.error("Basket can't be deleted")
    print('Basket removed!')
    self.update_basket(None)

  def do_list(self, inp):
    '''
list all baskets in server
    ''' 
    client = LanaClient(self.host, self.port)
    baskets = client.get_all_baskets()
    if baskets == None:
      return self.error('server error')
    if len(baskets) == 0:
      print('No baskets found\n')
      return      
    print("\nBaskets:")
    for b in baskets:
      print("  {}".format(b))
    print("")

  def do_exit(self, inp):
    ''' 
exit this awesome tool
    '''
    print('Bye')
    return True

  def emptyline(self):
    pass