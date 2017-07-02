# parsingaws


## usage :

```python
import json
from parse_aws.myaws import MyAws
data = json.load(open('datafile.json', 'r'))
myaws = MyAws(data)
myaws.compute_storage_repartition()
```

which outputs : 
```json
'[\n  {\n    "InstanceId": "i-1", \n    "TotalDataSize": 2508\n  }, \n  {\n    "InstanceId": "i-2", \n    "TotalDataSize": 2508\n  }, \n  {\n    "InstanceId": "i-3", \n    "TotalDataSize": 2508\n  }, \n  {\n    "InstanceId": "i-4", \n    "TotalDataSize": 2508\n  }, \n  {\n    "InstanceId": "i-5", \n    "TotalDataSize": 2508\n  }, \n  {\n    "InstanceId": "i-6", \n    "TotalDataSize": 2508\n  }, \n  {\n    "InstanceId": "i-7", \n    "TotalDataSize": 2508\n  }, \n  {\n    "InstanceId": "i-8", \n    "TotalDataSize": 2508\n  }\n]'
```