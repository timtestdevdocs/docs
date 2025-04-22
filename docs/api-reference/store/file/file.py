from jigsawstack import JigsawStack
import requests

# Initialize the JigsawStack client
jigsaw = JigsawStack(api_key="your-api-key")

# Fetch the image
response = requests.get("https://jigsawstack.com/preview/vocr-example.jpg")
blob = response.content

# Upload the file
upload_response = jigsaw.store.upload(
    blob,
    {
        "key": "new-image.jpg",
        "overwrite": True
    }
)
