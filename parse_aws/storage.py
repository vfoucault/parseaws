

class StorageVolumeAttachement(object):
    def __init__(self, attachment):
        self.instance_id = attachment["InstanceId"]
        self.volume_id = attachment["VolumeId"]
        self.device = attachment["Device"]


class StorageVolume(object):
    def __init__(self, storage_data):
        self.volume_id = storage_data["VolumeId"]
        self.size = storage_data["Size"]
        self.attachment = [StorageVolumeAttachement(bond) for bond in storage_data["Attachments"]]


class BlockDevice(object):
    def __init__(self, block_device_data, instance):
        self.device_name = block_device_data["DeviceName"]
        self.volume_id = block_device_data["Ebs"]["VolumeId"]
        self.instance = instance
        volume_candidate = next(iter(filter(lambda x: x.volume_id == self.volume_id, self.instance.myaws.storage_disks )), None)
        self.size = volume_candidate.size if volume_candidate else 0
        self.is_root = self.device_name == self.instance.root_disk
