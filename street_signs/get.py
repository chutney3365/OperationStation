import requests

api_key = 'hcP8IAJFdYp4o0lOSqSV'
workspace_name = "Operation Station"
project_name = 'operation-station-saayn/street-signs-oi59p'

base_url = 'https://api.roboflow.com/'

headers = {
    'Authorization': f'Bearer {api_key}'
}

# Get workspace ID
response = requests.get(f'{base_url}/workspaces', headers=headers)
workspaces = response.json()
workspace_id = None
for workspace in workspaces:
    if workspace == workspace_name:
        workspace_id = workspace["id"]
        break

if workspace_id is None:
    print(f"Error: Workspace '{workspace_name}' not found.")
    exit()

# Get projects in the workspace
response = requests.get(f'{base_url}/workspaces/{workspace_id}/projects', headers=headers)
projects = response.json()

# Check if the project named "street signs" exists in the workspace
project_exists = False
for project in projects:
    if project == project_name:
        project_exists = True
        break

if project_exists:
    print(f"Project '{project_name}' exists in workspace '{workspace_name}'.")
else:
    print(f"Project '{project_name}' does not exist in workspace '{workspace_name}'.")
