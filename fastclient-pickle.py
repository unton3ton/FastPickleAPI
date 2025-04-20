import requests

with open('data.pkl', 'rb') as input_file:
    files = {'input_file': input_file}
    response = requests.post('http://192.168.100.149:8000/forecast', files=files)

print(response.json())
