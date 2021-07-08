import json
# a = {"a":"skr", "b":"skrskr"}
# import json
#
# b = json.dumps(a)
# print(b)
# print(type(b))
#
b = {'status':'200', 'data':'<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <title>\u9996\u9875</title>\n</head>\n<body>\n<h1>\u4eba\u751f\u82e6\u77ed\uff0c\u6211\u7528python</h1>\n</body>\n</html>\n'}
c = "{\"status\": \"200\", \"data\": \"<!DOCTYPE html>\\n<html lang=\\\"en\\\">\\n<head>\\n    <meta charset=\\\"UTF-8\\\">\\n    <title>\\u9996\\u9875</title>\\n</head>\\n<body>\\n<h1>\\u4eba\\u751f\\u82e6\\u77ed\\uff0c\\u6211\\u7528python</h1>\\n</body>\\n</html>\\n\"}"
d = c.encode()

webjson = "{\"status\": \"200\", \"data\": \"<!DOCTYPE html>\\n<html lang=\\\"en\\\">\\n<head>\\n    <meta charset=\\\"UTF-8\\\">\\n    <title>\\u9996\\u9875</title>\\n</head>\\n<body>\\n<h1>\\u4eba\\u751f\\u82e6\\u77ed\\uff0c\\u6211\\u7528python</h1>\\n</body>\\n</html>\\n\"}"
webjsonencode = '"{\\"status\\": \\"200\\", \\"data\\": \\"<!DOCTYPE html>\\\\n<html lang=\\\\\\"en\\\\\\">\\\\n<head>\\\\n    <meta charset=\\\\\\"UTF-8\\\\\\">\\\\n    <title>\\\\u9996\\\\u9875</title>\\\\n</head>\\\\n<body>\\\\n<h1>\\\\u4eba\\\\u751f\\\\u82e6\\\\u77ed\\\\uff0c\\\\u6211\\\\u7528python</h1>\\\\n</body>\\\\n</html>\\\\n\\"}"'

print(json.dumps(b) == d)
print(json.dumps(b) == c)
print(c == webjson)
print(d == webjsonencode)