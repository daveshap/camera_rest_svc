# Camera REST microservice

Basic webcam REST microservice

# Usage

1. Run with `python camera.py`
2. Microservice periodically POSTs an image to the nexus microservice
3. Timestamp allows for precise calculations for services like SLAM

# Payload

The payload is JSON and consists of two primary components: `data` and `meta`

```json
{
"data": "<numpy cv2 image>",
"meta": {
	"time": "<UNIX timestamp>"
	}
}
```

This format of payload should be used for all cognitive microservice messages.
