#pip install requests
import requests
import sys

def getalltracks():
    endpoint='http://localhost:8000/Track/API/'
    method='GET'

    try:
        respo=requests.get(endpoint)
        print(respo.status_code)
        if(respo.status_code==202):
            for track in respo.json():
                print(f'ID:{{track["id"}},Name:{{track["name"]}}')
    except:
        print(sys.exc_info()[1])

getalltracks()


curl -X GET http://localhost:8000/Track/API/
