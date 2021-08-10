import json
import requests

def sending(data):
    with open("webhookAuth.json") as f:
        webhook_url = json.load(f)["url"]
    email = data["email"]
    name = data["name"]
    group = data["group"]
    contents = data["contents"]
    agree = data["agree"]
    text = f"연락처: {email}\n 성함: {name} \n소속: {group}\n상담신청내용: {contents}\n동의여부: {agree}"
    payload = {"text":text}
    requests.post(webhook_url, json=payload)