Lana command line client REST API

Requirements:
I've build it using Python 3.7 but any modern python will do it.
Virtual env is recommended but not mandatory.

I've added a small installdeps.sh file that configures venv and install dependencies but this may not be needed at all if you are using a complete python distro likes anaconda.
if you want to run in a virtual env environment run:
```
python3 -m venv .
source ./bin/activate
```
Then to install dependencies using pip run
```
pip3 install -r requirements.txt
```

After having all dependencies installed just run:

```
python3 lana-client.py
```

This asumes server is running on http://localhost:8080 to change this invoke script like this

```
python3 lana-client.py --host=http://api.server.com --port:80
```

Please not that http:// or https:// are needed as i haven't created a specific parameter for protocol.

This will open a REPL like interfase that will look similar to this:

```
Lana Basket Client
--

REPL tool to use with Lana's Basket Rest API

Usage:

new          : will add a new basket and select it
list         : will list available baskets)
use basket   : will select an existing basket. has autocompletation. just hit Tab
mug          : will add a 1 mug to basket. mug nn will add nn mugs to basket
pen          : will add a 1 pen to basket. pen nn will add nn pens to basket
tshirt       : will add a 1 tshirt to basket. tshirt nn will add nn tshirts to basket
total        : will show item details on basket and total cost including promotions.
remove       : will remove current basket

run help for command listing
run help <command> for help about a specific command


no basket > new
Basket 22ffbe71-d5fd-4ccf-986e-f137e8b7505f created!

basket: 22ffbe71-d5fd-4ccf-986e-f137e8b7505f > mug
1 MUGS in basket

basket: 22ffbe71-d5fd-4ccf-986e-f137e8b7505f > pen 2
2 PENS in basket

basket: 22ffbe71-d5fd-4ccf-986e-f137e8b7505f > total

Basket content:
  MUG    1
  PEN    2

Total basket cost is 12.50

basket: 22ffbe71-d5fd-4ccf-986e-f137e8b7505f > list

Baskets:
  69a22ff1-190e-4806-a975-da2d983a19ef
  78c5ae1c-bf1f-453c-8ab5-5ce415a034f4
  22ffbe71-d5fd-4ccf-986e-f137e8b7505f
  4985e1db-f20a-4778-96c6-49fd11144f0d

basket: 22ffbe71-d5fd-4ccf-986e-f137e8b7505f > use 78c5ae1c-bf1f-453c-8ab5-5ce415a034f4
basket changed to 78c5ae1c-bf1f-453c-8ab5-5ce415a034f4


Basket content:
  PEN    2
  TSHIRT 3

Total basket cost is 50.00

basket: 78c5ae1c-bf1f-453c-8ab5-5ce415a034f4 >
```