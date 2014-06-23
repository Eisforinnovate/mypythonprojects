import urllib

myurl = urllib.urlopen("http://google.ca")

print myurl

contents = myurl.readlines()

print contents

#get html returned


print contents[1:10]

headerinfo = myurl.info()
print headerinfo.getheader("date")
print headerinfo.getheader("content-type")


urllib.urlretreieve("http://google.ca", filename ="urlcontent")

