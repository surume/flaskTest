from unittest import TestCase
import applications.Service.redisService


class TestGetValueList(TestCase):
    def test_get_value_list(self):
        applications.Service.redisService.get_value_list("he")
        self.fail()