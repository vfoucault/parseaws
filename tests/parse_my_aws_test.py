import unittest2
from parse_aws.myaws import MyAws
from parse_aws.aws_instance import AwsInstance
from parse_aws.storage import StorageVolume
import json

dump = json.load(open("tests/resources/extract1.json"))

class TestFullAws(unittest2.TestCase):

    def test_with_sample_data(self):
        # Given
        raw_data = dump

        # When
        my_aws = MyAws(raw_data)

        # Then
        self.assertEquals(len(my_aws.instances), 8)
        self.assertEquals(len(my_aws.storage_disks), 17)
        self.assertIsInstance(my_aws.instances[0], AwsInstance)
        self.assertIsInstance(my_aws.storage_disks[0], StorageVolume)

if __name__ == '__main__':
    unittest2.main()