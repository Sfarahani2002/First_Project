import requests

response = requests.get("https://barnamenevisan.info/api/courses/getactivecourses")
# print(response)
# print(response.text)
data = response.text  #string
jsonData = response.json()
print(jsonData[0])

for course in jsonData:
    #print(course['title'])
    print(f"{course['title']} مدرس: {course['teacher']}")
    #print(course)

res = request.post("https://jsonplaceholder.typicode.com/posts")
print(res.json())

res = request.get("https://jsonplaceholder.typicode.com/comments?postId=0")
res = request.get("https://jsonplaceholder.typicode.com/comments", params={'postId' : 1})
print(res.json())

for data in res.json():
    print(data)

