# __init__.py

from src.signal_tower_server import Server
from src.driver.signal_tower_driver import Driver

server = Server("localhost", 9999, True)
server.start()