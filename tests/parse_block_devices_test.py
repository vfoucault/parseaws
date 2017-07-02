import unittest2
from parse_aws.storage import BlockDevice
import json

one_block_device = """{
"DeviceName": "/dev/xvda",
"Ebs": {
    "Status": "attached",
    "DeleteOnTermination": true,
    "VolumeId": "vol-1a",
    "AttachTime": "2017-02-21T17:19:10.000Z"
    }
}"""


class FakeMyAws(object):

    def __init__(self):
        self.name = "Fake myAws"
        self.instances = [FakeInstance(self)]
        self.storage_disks = [FakeStorageDisk()]

class FakeStorageDisk(object):

    def __init__(self):
        self.name = "fake storage disk"
        self.volume_id = "fake"


class FakeInstance(object):

    def __init__(self, myaws):
        self.name = "fake instance"
        self.root_disk = "/dev/xvdb"
        self.myaws = myaws

class TestParseVolumes(unittest2.TestCase):

    def test_create_volumes(self):
        # Given
        raw_volume = json.loads(one_block_device)
        myaws = FakeMyAws()

        # When
        volume = BlockDevice(raw_volume, myaws.instances[0])

        # Then
        self.assertEquals(volume.volume_id, "vol-1a")
        self.assertEquals(volume.device_name, "/dev/xvda")
        self.assertEquals(volume.size, 0) # We're not yet aware of the full topology

if __name__ == '__main__':
    unittest2.main()