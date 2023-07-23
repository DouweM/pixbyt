load("pixlib/file.star", "file")

def client.get_image():
    return file.read("logo.png")

def client.get_response(name):
    return file.exec("hello.py", {"name": name})["response"]
