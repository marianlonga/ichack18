########### Python 3.6 #############
import requests, base64

headers = {
    # Request headers.
    'Content-Type': 'application/octet-stream',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
    'Ocp-Apim-Subscription-Key': '7dc0a1103c3744fa80e5b1f8d72d8442',

    'Prediction-Key': '3cf083a425934f9eb7a63b8ce459ab3a',
}

params = {
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories',
    #'details': 'Celebrities',
    'language': 'en',
}

# Replace the three dots below with the full file path to a JPEG image of a celebrity on your computer or network.
image = open('Coca-Cola.jpg','rb').read() # Read image file in binary mode

try:
    # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the
    #   URL below with "westus".
    response = requests.post(#url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze',
                             url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/6ff322bf-f381-432a-88fb-1cd46474f39a/image?iterationId=669f7fbf-a7ed-4afe-9ce1-4f668c802e98',
                             headers = headers,
                             params = params,
                             data = image)
    data = response.json()
    label = data['Predictions'][0]['Tag']
    probability = data['Predictions'][0]['Probability']
    #category = data["Predictions"]["Tag"]
    #label = data['Predictions']['Tag']
    #probability = data['Predictions']['Probability']
    print(label, probability)
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################