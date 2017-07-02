from .storage import BlockDevice


class AwsInstance(object):
    def __init__(self,instance_data, myaws):
        self.myaws = myaws
        self.instance_name = instance_data['InstanceId']
        self.root_disk = instance_data["RootDeviceName"]
        self.disks = self.populate_disks(instance_data["BlockDeviceMappings"])

    def populate_disks(self, disks_data):
        return [BlockDevice(disk, self) for disk in disks_data]

    def get_total_storage(self, include_root=True):
        if include_root:
            total = sum([ disk.size for disk in self.disks])
        else:
            total = sum([ disk.size for disk in self.disks if not disk.is_root])
        return total

    def formated_raw_disk(self, include_root=True):
        total = self.get_total_storage(include_root=include_root)
        return {"InstanceId": self.instance_name, "TotalDataSize": total }

    def __repr__(self):
        return "<AwsInstance: id={} disks={} total_size={}".format(self.instance_name, len(self.disks), self.get_total_storage())