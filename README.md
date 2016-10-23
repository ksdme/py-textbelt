# Py-Textbelt #
Python Wrapper for Textbelt SMS API.

## Installation ##
This module is not currently available on any package manager, So just clone this repo and do ```import pytextbelt```.

## Usage ##
Example:
```
from pytextbelt import Textbelt

recepient = Textbelt.Recepient("1122334455", "us")
reponse = recepient.send("Hello World!")
reponse = recepient.send("Its me, The Bot.")
```

The construcor of Recepient Class: 
```def __init__(self, phone, region="us", tag = None)```, ```tag``` here helps maintain custom meta information on the Recepient object.

##### Available Properties: #####
 - ```recepient.phone```
 - ```recepient.region```
 - ```recepient.tag```

##### Supported Regions: #####
 - ```us``` (Defaulted)
 - ```ca``` (Canada)
 - ```intl``` (International)
