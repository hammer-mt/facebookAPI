import requests

# https://developers.facebook.com/tools/explorer/
app_id = "[redacted]"
app_secret = "[redacted]"
access_token = "[redacted]"
account_id = "[redacted]"

# https://developers.facebook.com/docs/marketing-api/insights/parameters/v10.0
fields = ['campaign_name', 'spend', 'impressions', 'clicks', 'actions', 'action_values']
url = f"https://graph.facebook.com/v10.0/act_{account_id}/insights"
params = {
    "access_token": access_token,
    "fields": ','.join(fields),
    "date_preset": "last_7d",
    "use_unified_attribution_setting": "true",
    "level": "campaign",
    "time_increment": "1"
}

res = requests.get(url=url, params=params)
json_data = res.json()
response = json_data['data']

paging = 'next' in json_data['paging']
while paging:
    next_url = json_data['paging']['next']
    res = requests.get(next_url)
    json_data = res.json()
    next_response = json_data['data']
    response += next_response
    paging = 'next' in json_data['paging']
