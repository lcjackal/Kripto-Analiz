from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from modules.websocket_handler import WebSocketHandler
from modules.data_fetcher import DataFetcher

class RadarTab(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Coin", "Son Fiyat", "Değişim (%)"])
        self.web_socket = None
        self.data_fetcher = None

    def start_real_time_updates(self, websocket_url, coinmarketcap_key, coingecko_key):
        # WebSocket setup for real-time updates
        self.web_socket = WebSocketHandler(websocket_url)
        self.web_socket.on_message = self.update_table_real_time
        self.web_socket.start()

        # DataFetcher setup for initial data
        self.data_fetcher = DataFetcher(coinmarketcap_key, coingecko_key)
        initial_data = self.data_fetcher.get_coin_data("BTC")  # Example to fetch BTC data
        self.populate_table(initial_data)

    def populate_table(self, data):
        self.setRowCount(1)
        self.setItem(0, 0, QTableWidgetItem(data.get("name", "Unknown")))
        self.setItem(0, 1, QTableWidgetItem(str(data.get("price", "N/A"))))
        self.setItem(0, 2, QTableWidgetItem("0.00"))  # Default change percentage

    def update_table_real_time(self, message):
        # Parse WebSocket message and update table
        data = message.get("product_id", {})
        for row in range(self.rowCount()):
            if self.item(row, 0).text() == data.get("name"):
                self.item(row, 1).setText(str(data.get("price", "N/A")))
                self.item(row, 2).setText(str(data.get("change", "0.00")))