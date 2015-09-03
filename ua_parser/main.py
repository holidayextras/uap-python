"""
    Wrapper around the python lib - pass in a string or a file of user agent strings
    Run:
        # python main.py <inputFormat: string|file> <uaString|inFilePath> <delimiter: \t|,|json> <outFilePath>

    E.g. from file woth :
    python main.py file ./random_user_agent_strings.txt , ./something_nice

    from user agent string:
    python main.py string "Mozilla/5.0 (Linux; Android 4.2.2; GT-I9195 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36" ,
"""

__author__ = 'viktor.trako@holidayextras.com (Viktor Trako)'

import sys
import user_agent_wrapper
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

if len(sys.argv) >= 4:
    inputType = sys.argv[1]
    inputFormat = sys.argv[2]
    delimiter = sys.argv[3]
    if len(sys.argv) == 5:
        inFilePath = inputFormat
        outFilePath = sys.argv[4]
    if inputType == 'string':
        parsedUaString = user_agent_wrapper.parseFromString(inputFormat, delimiter)
        print parsedUaString
    # pass it to string parser
    if inputType == 'file':
        user_agent_wrapper.parseFromFile(inFilePath, outFilePath, delimiter)
    else:
        sys.exit(1)
else:
    print 'Usage: main.py <user agent string>'
    sys.exit(1)
