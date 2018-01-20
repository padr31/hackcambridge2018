import requests

class AzureClient:

    def __init__(self):
        self.url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
        # https://westus.api.cognitive.microsoft.com/emotion/v1.0
        self.key = 'd4dac732849740fdb31c31b217463db2'
        self.maxNumRetries = 10


    def process_request(self, json, data, headers, params):
        retries = 0
        result = None

        while True:
            response = requests.request( 'post', self.url, json = json, data = data, headers = headers, params = params )

            if response.status_code == 429:
                if retries <= self.maxNumRetries:
                    time.sleep(1)
                    retries += 1
                    continue
                else:
                    break

            elif response.status_code == 200 or response.status_code == 201:
                if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                    result = None
                elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                    if 'application/json' in response.headers['content-type'].lower():
                        result = response.json() if response.content else None
                    elif 'image' in response.headers['content-type'].lower():
                        result = response.content
            else:
                print( "Error code: %d" % ( response.status_code ) )
                print( "Message: %s" % ( response.json()['error']['message'] ) )
            break

        return result

    def process_image(self, path_to_img):
        with open(path_to_img, 'rb') as f:
            data = f.read()

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self.key
        headers['Content-Type'] = 'application/octet-stream'

        json = None
        params = None
        result = self.process_request(json, data, headers, params)
        return result


# example use:
#   path_to_img = "/Users/markopuza/Downloads/IMG_20180120_131159.jpg"
#   ac = AzureClient()
#   response = ac.process_image(path_to_img)
