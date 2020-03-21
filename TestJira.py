import json

from jira import JIRA


jira = JIRA(server='https://jira.souban.io/', basic_auth=('zhangjian', 'b18666'))

issue = jira.issue('ATP-107')

print(type(json.loads(issue.raw['fields']['customfield_10206']['steps'][0]['data'])))