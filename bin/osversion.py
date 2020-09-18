"""osversion
"""
import os, wmi
from datetime import datetime

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2020-9-18"

class osversion:
	def __init__ (self, vs=False):
		"""The core of my project
		"""
		base_dir = "." if vs else ".." # the project "root" in Visual studio it is different

		log = open(os.path.join(base_dir, "log", "trace.log"), "a")
		csv_init = open(os.path.join(base_dir, "flussi", "PC_name.csv"), "r")
		csv_out = open(os.path.join(base_dir, "flussi", "PC_version.csv"), "w+")
		osversion.log(log, "Opened all files")
		#osversion.init_csv(csv_client, csv_server, log)
		
		start_time = datetime.now()
		osversion.log(log, f"Start time: {start_time}")
		osversion.log(log, "Running: osversion.py")

		csv_out.write(csv_init.read())

		"""conn = wmi.WMI()
		osversion.print_client(conn, log, csv_client)
		osversion.print_protocol(conn, log, csv_server)"""

		osversion.log(log, f"End time: {datetime.now()}\nTotal time: {datetime.now() - start_time}")
		osversion.log(log, "")
		log.close()

	def print_client(conn, log, csv):
		"""Prints the infos by Win32_NetworkClient
		"""
		osversion.log(log, " - Istruction: Win32_NetworkClient")
		for network_client in conn.Win32_NetworkClient(["Caption", "Description", "Status", "Manufacturer", "Name"]):
			print(network_client)
			osversion.log(log, f"   - {network_client.Caption}")
			csv.write(str(network_client.Caption) + ',' + str(network_client.Description) + ',' + str(network_client.Status) + ',' + str(network_client.Manufacturer) + ',' + str(network_client.Name) + '\n')

	def print_protocol(conn, log, csv):
		"""Prints the infos by Win32_NetworkProtocol
		"""
		osversion.log(log, " - Istruction: Win32_NetworkProtocol")
		for network_protocol in conn.Win32_NetworkProtocol(["Caption", "Description", "GuaranteesDelivery", "GuaranteesSequencing", "MaximumAddressSize", "MaximumMessageSize", "Name", "SupportsConnectData", "SupportsEncryption", "SupportsEncryption", "SupportsGracefulClosing", "SupportsGuaranteedBandwidth", "SupportsQualityofService"]):
			print(network_protocol)
			osversion.log(log, f"   - {network_protocol.Caption}")
			csv.write(str(network_protocol.Caption) + ',' + str(network_protocol.Description) + ',' + str(network_protocol.GuaranteesDelivery) + ',' + str(network_protocol.GuaranteesSequencing) + ',' + str(network_protocol.MaximumAddressSize) + ',' + str(network_protocol.MaximumMessageSize) + ',' + str(network_protocol.Name) + ',' + str(network_protocol.SupportsConnectData) + ',' + str(network_protocol.SupportsEncryption) + ',' + str(network_protocol.SupportsEncryption) + ',' + str(network_protocol.SupportsGracefulClosing) + ',' + str(network_protocol.SupportsGuaranteedBandwidth) + ',' + str(network_protocol.SupportsQualityofService) + '\n')

	def log(file, item):
		"""Writes a line in the log.log file
		"""
		file.write(f"{item}\n")

	def print_and_log(file, item):
		"""Writes on the screen and in the log file
		"""
		print(item)
		osversion.log(file, item)

	def init_csv(client, server, log):
		"""Init the csv files
		"""
		client.write("Caption,Description,Status,Manufacturer,Name\n")
		server.write("Caption,Description,GuaranteesDelivery,GuaranteesSequencing,MaximumAddressSize,MaximumMessageSize,Name,SupportsConnectData,SupportsEncryption,SupportsEncryption,SupportsGracefulClosing,SupportsGuaranteedBandwidth,SupportsQualityofService\n")
		osversion.log(log, "csv now initialized")


if __name__ == "__main__":
	# debug flag
	debug = True

	osversion(debug)
