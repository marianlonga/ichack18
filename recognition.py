import requests, base64
import time

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '7dc0a1103c3744fa80e5b1f8d72d8442',
    'Prediction-Key': '3cf083a425934f9eb7a63b8ce459ab3a',
}

params = {
    # optional
    'visualFeatures': 'Categories',
    'language': 'en',
}


photo_number = 1
while True:

    #image = open('Coca-Cola.jpg','rb').read() # Read image file in binary mode
    image = open('testing/test_' + str(photo_number) + '.jpg', 'rb').read()

    label, probability = 'none', 0

    try:
        response = requests.post(url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/6ff322bf-f381-432a-88fb-1cd46474f39a/image?iterationId=669f7fbf-a7ed-4afe-9ce1-4f668c802e98',
                                 headers = headers,
                                 params = params,
                                 data = image)
        data = response.json()
        #print(data)
        label = data['Predictions'][0]['Tag']
        probability = data['Predictions'][0]['Probability']

        #print(label, probability)
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


    print(photo_number, label, probability)


    photo_number += 1

    time.sleep(3)