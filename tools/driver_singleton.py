from config.constants import INSTANCE_ATTR, DRIVER_ATTR
from tools.driver_factory import DriverFactory


class DriverSingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, INSTANCE_ATTR):
            cls.instance = super(DriverSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, driver_name):
        if not hasattr(self, DRIVER_ATTR):
            self.driver = DriverFactory.get_driver(driver_name)

    def get_driver(self):
        return self.driver
