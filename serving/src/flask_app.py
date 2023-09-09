from flask import Flask
import socket
from uuid import uuid4


app = Flask(__name__)


def get_details_of_host():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return (f"<b>hostname:</b> {host_name}<br>"
            f"<b>hostip:</b> {host_ip}<br>"
            f"<b>ID:</b> {uuid4()}")


@app.route("/health")
def health():
    return f"Server is healthy"


@app.route("/", methods=["GET", "POST"])
def default():
    return get_details_of_host()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010, debug=True)
