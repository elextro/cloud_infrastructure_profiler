import unittest
import yaml
import sys
from osprofiler.osprofiler import PluginLoader


class TestPluginLoader(unittest.TestCase):

    def setUp(self):
        print "setup method is being called"
        CONFIG_FILE = "../test-config.conf"

        sys.path.insert(0, "../../plugins")

        # Eventually we can test to see if a bad yaml file
        # Raises an exception.
        with open(CONFIG_FILE, 'r') as f:
            config = f.read()

        # Loading the yaml config file to a python dict
        config = yaml.load(config)
        self.config = config

        self.loader = PluginLoader(config)

    # Test load_plugins method
    def test_load_plugins(self):
        """
        This method tests to see if the load plugins method
        returns a dict of the proper form:

        {"string": <OBJ>, "string2": <OBJ>, ... , "stringN", <OBJ> }

        where N is the number of agents that have been loaded from
        the config
        """
        self.agent_object_dict = self.loader.load_plugins()
        # Checking to see if the returned value is a dict
        self.assertTrue(isinstance(self.agent_object_dict, dict))

        # Verifying the values of the dict
        for agent, agent_obj in self.agent_object_dict.iteritems():

            # Testing the type of keys returned by PluginLoader
            # Should be string
            self.assertTrue(isinstance(agent, str))

            # Testing to see if agent loaded matches the object attributes.
            # The agent object's name attribute should match
            # what PluginLoader returns
            process_config = getattr(agent_obj, "agent_config")
            self.assertTrue(agent == process_config['name'])


if __name__ == '__main__':
    unittest.main()
#  suite = unittest.TestLoader().loadTestsFromTestCase(TestPluginLoader)
#  result = unittest.TestResult()
#  suite.run(result)
#  print result
