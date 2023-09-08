from flask import Flask
import socket

app = Flask(__name__)


def get_details_of_host():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return f"hostname: {host_name}, hostip: {host_ip}"


@app.route("/", methods=["GET", "POST"])
def default():
    return get_details_of_host()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010, debug=True)
