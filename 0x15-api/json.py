#!/usr/bin/python3
""" Export api to csv"""
import json
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    api_url = 'https://jsonplaceholder.typicode.com/users/' + user
    response = requests.get(api_url)
    user_name = response.json().get('username')