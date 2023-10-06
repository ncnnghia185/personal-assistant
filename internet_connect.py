import socket
import wikipedia


def check_internet_connection():
    IPAddress = socket.gethostbyname(socket.gethostname())
    if IPAddress == "127.0.0.1":
        return False
    else:
        return True


def check_on_wikipedia(query):
    query = query.lower()
    query = query.replace("who is ", "")
    query = query.replace("what is ", "")
    query = query.replace("where is ", "")
    query = query.replace("tell me about ", "")
    query = query.replace("do you know ", "")
    query = query.strip()
    try:
        data = wikipedia.summary(query, sentences=8)
        return data
    except Exception as e:
        return ""
