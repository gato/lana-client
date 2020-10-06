Lana command line client (for REST API)

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

new          : add a new basket and select it
list         : list available baskets)
use basket   : select an existing basket. has autocompletation. just hit Tab
mug          : add a 1 mug to basket. mug nn will add nn mugs to basket
pen          : add a 1 pen to basket. pen nn will add nn pens to basket
tshirt       : add a 1 tshirt to basket. tshirt nn will add nn tshirts to basket
total        : show item details on basket and total cost including promotions.
remove       : remove current basket
exit         : self explanatory

run help for command listing
run help <command> for help about a specific command


no basket > new
Basket ba10e5a9-56c8-4497-bf67-1c265c369911 created!

basket: ba10e5a9-56c8-4497-bf67-1c265c369911 > pen
1 PENS in basket

basket: ba10e5a9-56c8-4497-bf67-1c265c369911 > tshirt
1 TSHIRTS in basket

basket: ba10e5a9-56c8-4497-bf67-1c265c369911 > mug
1 MUGS in basket

basket: ba10e5a9-56c8-4497-bf67-1c265c369911 > total

Basket content:
  PEN    1
  TSHIRT 1
  MUG    1

Total basket cost is 32.50€

basket: ba10e5a9-56c8-4497-bf67-1c265c369911 > new
Basket 66ad0779-b99f-47ad-822a-01429032135c created!

basket: 66ad0779-b99f-47ad-822a-01429032135c > pen
1 PENS in basket

basket: 66ad0779-b99f-47ad-822a-01429032135c > tshirt
1 TSHIRTS in basket

basket: 66ad0779-b99f-47ad-822a-01429032135c > pen
2 PENS in basket

basket: 66ad0779-b99f-47ad-822a-01429032135c > total

Basket content:
  TSHIRT 1
  PEN    2

Total basket cost is 25.00€

basket: 66ad0779-b99f-47ad-822a-01429032135c > new
Basket d65cf931-0d2b-486a-8e7a-fe229d6d10d0 created!

basket: d65cf931-0d2b-486a-8e7a-fe229d6d10d0 > tshirt 3
3 TSHIRTS in basket

basket: d65cf931-0d2b-486a-8e7a-fe229d6d10d0 > pen
1 PENS in basket

basket: d65cf931-0d2b-486a-8e7a-fe229d6d10d0 > tshirt
4 TSHIRTS in basket

basket: d65cf931-0d2b-486a-8e7a-fe229d6d10d0 > total

Basket content:
  TSHIRT 4
  PEN    1

Total basket cost is 65.00€

basket: d65cf931-0d2b-486a-8e7a-fe229d6d10d0 > new
Basket 1126ab90-cc03-4afc-8b37-501f3f6a8420 created!

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > pen
1 PENS in basket

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > tshirt
1 TSHIRTS in basket

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > pen
2 PENS in basket

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > pen
3 PENS in basket

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > mug
1 MUGS in basket

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > tshirt
2 TSHIRTS in basket

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > tshirt
3 TSHIRTS in basket

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > total

Basket content:
  PEN    3
  TSHIRT 3
  MUG    1

Total basket cost is 62.50€

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > list

Baskets:
  4985e1db-f20a-4778-96c6-49fd11144f0d
  ba10e5a9-56c8-4497-bf67-1c265c369911
  66ad0779-b99f-47ad-822a-01429032135c
  d65cf931-0d2b-486a-8e7a-fe229d6d10d0
  7274db3b-1f12-4b08-9da8-f61bfd570f60
  1126ab90-cc03-4afc-8b37-501f3f6a8420
  69a22ff1-190e-4806-a975-da2d983a19ef
  78c5ae1c-bf1f-453c-8ab5-5ce415a034f4
  22ffbe71-d5fd-4ccf-986e-f137e8b7505f
  dd091105-498c-4a74-93c6-437273bcfbee

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > use d65cf931-0d2b-486a-8e7a-fe229d6d10d0
basket changed to d65cf931-0d2b-486a-8e7a-fe229d6d10d0


Basket content:
  TSHIRT 4
  PEN    1

Total basket cost is 65.00€

basket: d65cf931-0d2b-486a-8e7a-fe229d6d10d0 > remove

*******
You are going to remove basket d65cf931-0d2b-486a-8e7a-fe229d6d10d0

Basket content:
  TSHIRT 4
  PEN    1

Total basket cost is 65.00€


Are you sure [Y/N]? Y
Basket removed!
no basket > use 1126ab90-cc03-4afc-8b37-501f3f6a8420
basket changed to 1126ab90-cc03-4afc-8b37-501f3f6a8420


Basket content:
  MUG    1
  PEN    3
  TSHIRT 3

Total basket cost is 62.50€

basket: 1126ab90-cc03-4afc-8b37-501f3f6a8420 > exit
Bye
```