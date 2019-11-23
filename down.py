import re as re2
import requests as req
import os


#get the response
re = req.get('http://www.cs.cornell.edu/courses/cs4670/2015sp/lectures/lectures.html')
ret = re.text
#print(re.text)
m = re2.findall(r'<td><a href=" (.*?).pdf">',ret)
#print(m[0])
n = len(m)
command_head = "wget "
url_head = "http://www.cs.cornell.edu/courses/cs4670/2015sp/lectures/"
for i in range(n-2):
    url_list = [url_head,m[i],'.pdf']
    a = ''
    down_url = a.join(url_list)
    command_list = [command_head, down_url]
    b = ''
    command = b.join(command_list)
    os.system(command)




     






