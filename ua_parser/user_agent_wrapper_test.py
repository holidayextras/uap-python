"""User Agent Wrapper unit tests
RUN:
python -m user_agent_wrapper_test ParseStringWithGivenDelimiter
or run all:
python -m user_agent_wrapper_test
"""

__author__ = 'viktor.trako@holidayextras.com (Viktor Trako)'

import os
import unittest
import json

import user_agent_wrapper

TEST_RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                  '../uap-core/test_resources')
ROOT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))

class ParseStringWithGivenDelimiter(unittest.TestCase):
    def testUserAgentStringsFromFile(self):
        self.runParseUserAgentStringsFromFile(os.path.join(
            TEST_RESOURCES_DIR, 'random_user_agent_strings.txt'), os.path.join(
            os.path.abspath(os.path.dirname(__file__)), './ua_out_file'))

    def testUserAgentStringFromString(self):
        self.runParserUserAgentStringFromStringAsJson()

    def runParserUserAgentStringFromStringAsJson(self):

        userAgentString = "Mozilla/5.0 (Linux; Android 4.2.2; GT-I9195 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36"
        delimiter = "json"

        expected = {
            "device":{
                "family":"Samsung GT-I9195"
            },
            "os":{
                "major":"4",
                "patch_minor": None,
                "minor":"2",
                "family":"Android",
                "patch":"2"
            },
            "user_agent":{
                "major":"44",
                "minor":"0",
                "family":"Chrome Mobile",
                "patch":"2403"
            },
            "string":"Mozilla/5.0 (Linux; Android 4.2.2; GT-I9195 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36"
        }

        result = json.loads(user_agent_wrapper.parseFromString(userAgentString, delimiter))
        device = expected['device']['family']
        os = expected['os']['family'];
        browser = expected['user_agent']['family'];
        string = expected['string'];

        self.assertEqual(device, result['device']['family'])
        self.assertEqual(os, result['os']['family'])
        self.assertEqual(browser, result['user_agent']['family'])
        self.assertEqual(string, result['string'])

    def runParseUserAgentStringsFromFile(self, inFilePath, outFilePath):
        delimiter = ","
        user_agent_wrapper.parseFromFile(inFilePath, outFilePath, delimiter)
        numLines = sum(1 for line in open(os.path.join(ROOT_DIR, 'ua_out_file')))

        self.assertTrue(os.path.isfile(os.path.join(ROOT_DIR, 'ua_out_file')))
        self.assertTrue(os.stat(os.path.join(ROOT_DIR, 'ua_out_file')).st_size > 0)
        self.assertEqual(numLines, 100)

if __name__ == '__main__':
    unittest.main()
