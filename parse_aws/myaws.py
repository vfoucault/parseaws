import json

from .aws_instance import AwsInstance
from .storage import *


class MyAws(object):

    def __init__(self, instances_data):
        self.storage_disks = [StorageVolume(volume) for volume in instances_data['Volumes']]
        self.instances = self.__init_instances(instances_data["Reservations"])

    def __init_instances(self, reservations):
        return_data = []
        owners = [owner for owner in reservations]
        for owner in owners:
            return_data.append(map(lambda x: AwsInstance(x, myaws=self), owner["Instances"]))
        return sum(return_data, [])

    def compute_storage_repartition(self, include_root=True):
        data = [x.formated_raw_disk(include_root=include_root) for x in self.instances]
        return json.dumps(data, sort_keys=True, indent=2)