import datetime
import json
from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
from django.core.serializers.json import DjangoJSONEncoder
from .models import Issues  # Ensure you import your model

# JIRA Credentials
JIRA_URL = "https://mandolaharshad6.atlassian.net"
Api_Token = "ATATT3xFfGF0vBXP_13pHEhpn4CQYgvqizXs3T95JDNfoCwt7DU-UcESOKZrZID3ZXi04Mq0IIxR5EAk3TWRFrctZywN1CwW0-dWLZZK8qnCocQAISmBpK19dYSDUxEz2ERoFy95ARchTlLIfBehWMg_1Ip_k1NyM0x9CJ_HQskmnYsYvc4A7sc=1E4F1E2E"
Email = "mandolaharshad6@gmail.com"
Project_Key = "DP"
Jira_API_url = f"{JIRA_URL}/rest/api/3/search?jql=project%3D{Project_Key}"

# Fetch Data from JIRA
def fetch_jira_data():
    auth = HTTPBasicAuth(Email, Api_Token)
    headers = {"Accept": "application/json"}
    response = requests.get(url=Jira_API_url, headers=headers, auth=auth)

    if response.status_code == 200:
        data = response.json()
        return data.get("issues", [])  # Ensure it returns a list
    else:
        print("Error:", response.status_code, response.text)
        return []

# Django View
def jira_view(request):
  
    issues = fetch_jira_data()
    

    for issue in issues:
        Issues.objects.get_or_create(
            issue_id=issue["id"],
            issue_key=issue["key"],
            created_date=issue['fields'].get('created', None),
            name=issue["fields"].get("name", "noname")
        )

    # Retrieve Issues from DB and convert datetime to string
    issues_list = list(Issues.objects.values("issue_id", "issue_key", "created_date"))
    
    for issue in issues_list:
        if issue["created_date"]:
            issue["created_date"] = issue["created_date"].isoformat()  # Convert datetime to string
   
    # Pass JSON Data Safely
    context = {
        "issues": json.dumps(issues_list, cls=DjangoJSONEncoder),
        "total_issues": Issues.objects.count()
    }

    return render(request, 'harrychart/datatable.html', context)
