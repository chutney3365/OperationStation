import roboflow

rf = roboflow.Roboflow(api_key='hcP8IAJFdYp4o0lOSqSV')

# List all projects for your workspace
workspace = rf.workspace()

print(workspace)