## A simple parser service

Workflow:

- Downloads sample image from the web ->
- Writes the image to disk ->
- Saves image metadata to database ->
- Sends image_id to message queue for further processing.
