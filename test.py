# import requests module
import requests
 
# Making a get request
# response = requests.get('https://expired.badssl.com/', verify = False)
data = {"operationName":"test","variables":{},"query":"query test {  users {   id  }}"}

r = requests.post(url = "https://api.review-ty.com/graphql", data = data, verify = False)
  
# extracting response text 
pastebin_url = r.text

# print request object
print(pastebin_url)
