from roboflow import Roboflow

rf = Roboflow(api_key="hcP8IAJFdYp4o0lOSqSV")
project = rf.workspace().project("operation-station-saayn/street-signs-oi59p")
model = project.version(1).model

# infer on a local image
print(model.predict("road403.jpg", confidence=50, overlap=50).json())

