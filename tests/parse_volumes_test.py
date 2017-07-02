import unittest2
from parse_aws.storage import StorageVolume
import json

one_volume = """{
    "AvailabilityZone": "eu-west-1c",
    "Attachments": [
        {
            "AttachTime": "2017-02-21T17:21:07.000Z",
            "InstanceId": "i-",
            "VolumeId": "vol-4b",
            "State": "attached",
            "DeleteOnTermination": true,
            "Device": "/dev/xvdb"
        }
    ],
    "Tags": [
        {
            "Key": "tag_key",
            "Value": "tag_value"
        },
        {
            "Key": "tag_key",
            "Value": "tag_value"
        },
        {
            "Key": "tag_key",
            "Value": "tag_value"
        }
    ],
    "Encrypted": false,
    "VolumeType": "gp2",
    "VolumeId": "vol-4b",
    "State": "in-use",
    "Iops": 7500,
    "SnapshotId": "snap-",
    "CreateTime": "2017-02-21T17:21:01.168Z",
    "Size": 2500
}"""

class TestParseBlockDevice(unittest2.TestCase):

    def test_create_block_device(self):
        # Given
        raw_volume = json.loads(one_volume)

        # When
        volume = StorageVolume(raw_volume)

        # Then
        self.assertEquals(volume.volume_id, "vol-4b")
        self.assertEquals(volume.size, 2500)
        self.assertEquals(len(volume.attachment), 1)


if __name__ == '__main__':
    unittest2.main()