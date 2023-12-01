# from star war API, requests 20 planets' data

import requests
import time
import pandas as pd

planet = pd.DataFrame()

for i in range(20) :
    url = f"https://swapi.dev/api/planets/{i+1}"

    res = requests.get(url)
                       
    if(res.status_code == 200) :
        data = res.json() 
        df = pd.DataFrame.from_records(
            [
            {
            "id" : i+1,
            "name" : data['name'],
            "diameter" : data['diameter'], 
            "gravity" : data['gravity'],
            "surface_water" : data['surface_water'],
            "population" : data['population']
            }
            ], index = "id" )
        planet = pd.concat([planet, df])
        time.sleep(0.5)
       
planet        
