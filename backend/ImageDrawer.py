from AzureClient import AzureClient
import cv2

class ImageDrawer:
    def draw_image(self, json, data, headers, params):
        result = AzureClient().process_request(json, data, headers, params)
        if result is not None:
            # Load the original image from disk
            data8uint = np.fromstring(data, np.uint8)  # Convert string to an unsigned int array
            img = cv2.cvtColor(cv2.imdecode(data8uint, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)

            renderResultOnImage(result, img)

            ig, ax = plt.subplots(figsize=(15, 20))
            ax.imshow(img)