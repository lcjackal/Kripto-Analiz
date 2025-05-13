import websocket
import json
import threading

class WebSocketHandler:
    def __init__(self, url):
        self.url = url
        self.ws = None
        self.thread = None

    def on_message(self, ws, message):
        data = json.loads(message)
        print(f"Real-time data received: {data}")

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")

    def on_open(self, ws):
        print("WebSocket connection opened")
        # Example subscription message (modify as needed)
        subscription_message = {
            "type": "subscribe",
            "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
        }
        ws.send(json.dumps(subscription_message))

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.thread = threading.Thread(target=self.ws.run_forever, daemon=True)
        self.thread.start()

    def stop(self):
        if self.ws:
            self.ws.close()
        if self.thread and self.thread.is_alive():
            self.thread.join()