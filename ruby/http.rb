require 'open-uri'

uri = open('http://www.baidu.com/')
response_status = uri.status
#response_body = uri.read[559, 441]

puts response_status
#puts response_body