from roboflow import Roboflow

rf = Roboflow(api_key="rf_WBGHxj31NrTtNloPbJUvKDGLmQC3")
project = rf.workspace().project("street signs")
model = project.version(1).model

# infer on a local image
print(model.predict("road403.jpg", confidence=50, overlap=50).json())