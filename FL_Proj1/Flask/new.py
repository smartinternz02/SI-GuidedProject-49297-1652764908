import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "CqdpDnaejr5skzGOvKI5wrS57NGHwueNpUUcN7xj-ael"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["name","month","dayofmonth","dayofweek","origin0","origin1","origin2","origin3","origin4","destination0","destination1","destination2","destination3","destination4","scheduleddeparturetime","actualdeparturetime"],"values":[[1399,1,2,6,0,0,0,0,1,0,1,0,0,0,30,12]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/c7bb6cfa-ffd0-4e1d-b45a-3626bc5a29b7/predictions?version=2022-07-23', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
#print(response_scoring.json())
pred=response_scoring.json()
output=pred['predictions'][0]['values'][0][0]
print(output)
