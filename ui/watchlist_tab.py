from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
from modules.data_fetcher import DataFetcher

class WatchlistTab(QWidget):
    def __init__(self, coinmarketcap_key, coingecko_key, parent=None):
        super().__init__(parent)
        self.data_fetcher = DataFetcher(coinmarketcap_key, coingecko_key)

        # Layout
        self.layout = QVBoxLayout(self)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Coin", "Sembol", "Son Fiyat", "Kontrat", "Ağ"])
        self.layout.addWidget(self.table)

        # Add Button
        self.add_button = QPushButton("Coin Ekle")
        self.add_button.clicked.connect(self.add_coin)
        self.layout.addWidget(self.add_button)

    def add_coin(self):
        # Example: Adding Bitcoin to the table
        coin_data = self.data_fetcher.get_coin_data("BTC")
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(coin_data.get("name", "Unknown")))
        self.table.setItem(row_position, 1, QTableWidgetItem(coin_data.get("symbol", "N/A")))
        self.table.setItem(row_position, 2, QTableWidgetItem(str(coin_data.get("price", "N/A"))))
        self.table.setItem(row_position, 3, QTableWidgetItem(coin_data.get("contract", "N/A")))
        self.table.setItem(row_position, 4, QTableWidgetItem(coin_data.get("network_logo", "N/A")))