import sys
import requests

resposnse = requests.get("https://www.youtube.com/watch?v=MztLZWibctI&list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V&index="+sys.argv[1])

print(resposnse.json())
