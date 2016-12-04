# Py-Textbelt #
Python Wrapper for Textbelt SMS API.

## Installation ##
This module is not currently available on any package index, So just clone this repo and do ```import pytextbelt```.

## Usage ##
Example:
```
from pytextbelt import Textbelt

Recipient = Textbelt.Recipient("1122334455", "us")
reponse = Recipient.send("Hello World!")
reponse = Recipient.send("Its me, The Bot.")
```

The construcor of Recipient Class: 
```def __init__(self, phone, region="us", tag = None)```, ```tag``` here helps maintain custom meta information on the Recipient object.

##### Available Properties: #####
 - ```Recipient.phone```
 - ```Recipient.region```
 - ```Recipient.tag```

##### Supported Regions: #####
 - ```us``` (Defaulted)
 - ```ca``` (Canada)
 - ```intl``` (International)
