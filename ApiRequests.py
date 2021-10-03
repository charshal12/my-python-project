import requests

response = requests.get("https://gitlab.com/api/v4/users/charshal12/projects/")
my_project = response.json()
# print(type(response.json))
# print(response.json()[0])

for project in my_project:
    print(f"Project Name : {project['name']} \nProject URL : {project['web_url']}\n")

