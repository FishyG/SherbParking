#!/usr/bin/env python3

import json
import requests


url = "https://www.sherbrooke.ca/api/entity/get-entity-module-listing"
payload = [{"entityModuleId":"333ac637-bf6e-e611-80ed-00155d09650f"}]

def main():

    r = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    
    print(r.json()["value"][0]["name"]["en"])
    
    # Extract the state of the night parking from the massive json
    night_parking = r.json()["value"][0]["listing"][0]["categories"]["base"][0]["name"]["en"]
    
    print(night_parking)
 

if __name__ == '__main__':
    main()

