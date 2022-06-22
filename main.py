import os
import argparse 
import requests

def previous():
    requests.get("http://localhost:9000/api/playback/previous")
def playpause():
    requests.get("http://localhost:9000/api/playback/playpause")
def next():
    requests.get("http://localhost:9000/api/playback/next")
def ampp_main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-a', '--action', help='repo help', required=True)
    args = parser.parse_args()

    if (args.action == "left"):
        previous()
    elif (args.action == "right"):
        next()
    elif (args.action == "play"):
        playpause()
    



ampp_main()
