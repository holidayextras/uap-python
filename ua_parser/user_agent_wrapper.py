"""
    Wrapper around the python lib - pass in a string or a file of user agent strings
    Run:
        # python main.py <inputFormat: string|file> <uaString|filePath> <delimiter: \t|,|json>
    When running from file, the output file with generate a file with the following headers:
    user_agent,device,os,os_major,os_minor,os_patch_minor,os_patch,browser,browser_major,browser_minor,browser_patch
"""
from numpy.lib.arraysetops import in1d

__author__ = 'viktor.trako@holidayextras.com (Viktor Trako)'

from ua_parser import user_agent_parser
import json
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)


def parseFromFile(inFilePath, outFilePath, delimiter):
    "Parse user agents using a file input"
    # return parseUaString(filePath, delimiter)
    inFileOpen = open(inFilePath, "r")
    outFileOpen = open(outFilePath, "wb")
    outFileOpen.write("user_agent"+delimiter+\
                    "device"+delimiter+\
                      "os"+delimiter+\
                      "os_major"+delimiter+\
                      "os_minor"+delimiter+\
                      "os_patch_minor"+delimiter+\
                      "os_patch"+delimiter+\
                      "browser"+ delimiter+\
                      "browser_major"+ delimiter+\
                      "browser_minor"+delimiter+\
                      "browser_patch\n")
    for line in inFileOpen:
        parsedUaString = parseUaString(line, delimiter)
        outFileOpen.write(str(parsedUaString+'\n'))
    inFileOpen.close()
    outFileOpen.close()


def parseFromString(uaString, delimiter):
    "Parse user agents using a file input"
    return parseUaString(uaString, delimiter)


def parseUaString(str, delimiter):
    "Use the provided lib to parse the user agent string"
    # print 'UA String to Parse =', sys.argv[1]
    # On the server, you could use a WebOB request object.
    # user_agent_string = request.META.get('HTTP_USER_AGENT')

    # def main(argv):

    # For demonstration purposes, though an iPhone ...
    # user_agent_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
    user_agent_string = str
    # Get back a big dictionary of all the goodies.
    result_dict = user_agent_parser.Parse(user_agent_string)

    uaJson = json.dumps(result_dict, separators="," ":")

    # print json.dumps(result_dict['user_agent'], separators="," ":")
    # {'major': '5', 'minor': '1', 'family': 'Mobile Safari', 'patch': None}

    # print json.dumps(result_dict['os'], separators="," ":")
    # {'major': '5', 'patch_minor': None, 'minor': '1', 'family': 'iOS', 'patch': None}

    # print json.dumps(result_dict['device'], separators="," ":")
    # {'family': 'iPhone'}
    # print '__name__ = ', __name__
    if delimiter == "json":
        return uaJson
    if delimiter == "\\t" or delimiter == ",":
        user_agent = json.dumps(result_dict['string'], separators="," ":")
        device = json.dumps(result_dict['device']['family'], separators="," ":")
        os = json.dumps(result_dict['os']['family'], separators="," ":")
        os_major = json.dumps(result_dict['os']['major'], separators="," ":")
        os_minor = json.dumps(result_dict['os']['minor'], separators="," ":")
        os_patch_minor = json.dumps(result_dict['os']['patch_minor'], separators="," ":")
        os_patch = json.dumps(result_dict['os']['patch'], separators="," ":")
        browser = json.dumps(result_dict['user_agent']['family'], separators="," ":")
        browser_major = json.dumps(result_dict['user_agent']['major'], separators="," ":")
        browser_minor = json.dumps(result_dict['user_agent']['minor'], separators="," ":")
        browser_patch = json.dumps(result_dict['user_agent']['patch'], separators="," ":")

        return user_agent+delimiter+\
                device + delimiter+\
                os+ delimiter+\
                os_major+ delimiter+\
                os_minor+ delimiter+\
                os_patch_minor+ delimiter+\
                os_patch+ delimiter+\
                browser+ delimiter+\
                browser_major+ delimiter+\
                browser_minor+ delimiter+\
                browser_patch

    else:
        return "Unknown delimiter"
