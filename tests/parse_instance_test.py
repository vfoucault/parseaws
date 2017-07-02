import unittest2
from parse_aws.myaws import MyAws
from parse_aws.aws_instance import AwsInstance
from parse_aws.storage import StorageVolume
import json

dump = json.load(open("tests/resources/extract1.json"))

class TestFirstInstance(unittest2.TestCase):

    def test_with_sample_data(self):
        # Given
        raw_data = dump

        # When
        my_aws = MyAws(raw_data)

        # Then
        first_instance = [x for x in my_aws.instances if x.instance_name == "i-1"][0]
        self.assertEquals(first_instance.instance_name, "i-1" )
        self.assertEquals(first_instance.root_disk, "/dev/xvda")
        self.assertEquals(len(first_instance.disks), 2)
        self.assertEquals(first_instance.get_total_storage(), 2508)
        self.assertEquals(first_instance.get_total_storage(include_root=False), 2500)
        self.assertEquals(first_instance.formated_raw_disk(), {"InstanceId": "i-1", "TotalDataSize": 2508})

if __name__ == '__main__':
    unittest2.main()