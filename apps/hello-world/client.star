load("pixlib/file.star", "file")

def client.get_image():
    return file.read("logo.png")

def client.get_response(name):
    input = {"name": name}
    output = file.exec("hello.py", input)

    print("%s ---hello.py--> %s" % (input, output))

    return output["response"]
