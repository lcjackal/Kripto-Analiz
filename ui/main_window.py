from PyQt5.QtWidgets import QMainWindow, QTabWidget
from ui.radar_tab import RadarTab
from ui.watchlist_tab import WatchlistTab

class MainWindow(QMainWindow):
    def __init__(self, coinmarketcap_key, coingecko_key, websocket_url):
        super().__init__()
        self.setWindowTitle("Kripto Analiz Uygulaması")
        self.resize(800, 600)

        # Tab Widget
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Add Radar Tab
        self.radar_tab = RadarTab()
        self.tabs.addTab(self.radar_tab, "Pump/Dump Radar")

        # Add Watchlist Tab
        self.watchlist_tab = WatchlistTab(coinmarketcap_key, coingecko_key)
        self.tabs.addTab(self.watchlist_tab, "İzleme Listesi")

        # Start real-time updates
        self.radar_tab.start_real_time_updates(websocket_url, coinmarketcap_key, coingecko_key)