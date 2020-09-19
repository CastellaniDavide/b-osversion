"""osversion
"""
import os, wmi
from datetime import datetime

__author__ = "help@castellanidavide.it"
__version__ = "01.01 2020-9-18"

class osversion:
	def __init__ (self, debug=False):
		"""The core of my project
		"""
		base_dir = "." if debug else ".." # the project "root" in Visual studio it is different

		# Open files
		log = open(os.path.join(base_dir, "log", "trace.log"), "a")
		csv_in = open(os.path.join(base_dir, "flussi", "PC_name.csv"), "r")
		csv_out = open(os.path.join(base_dir, "flussi", "PC_version.csv"), "w+")

		osversion.log(log, "Opened all files")
		osversion.init_csv(csv_in, csv_out, log)
		
		# Start time
		start_time = datetime.now()
		osversion.log(log, f"Start time: {start_time}")
		osversion.log(log, "Running: osversion.py")

		# Core operations
		osversion.print_OS_Info(log, csv_in, csv_out, debug)

		# End
		osversion.log(log, f"End time: {datetime.now()}\nTotal time: {datetime.now() - start_time}")
		osversion.log(log, "")
		log.close()
		csv_in.close()
		csv_out.close()

	def print_OS_Info(log, csv_in, csv_out, debug):
		"""Prints the infos by Win32_OperatingSystem
		"""
		osversion.print_and_log(log, " - Get OS and OS version in:")
		
		# Only on the PC if debug is true, else on all PCs in the list
		for PC_name in ("My PC, debug option",) if debug else csv_in.read().split("\n")[1:]:
			# Establish a new connection
			conn = wmi.WMI("" if debug else PC_name)

			# Get the necessary infos
			for os_info in conn.Win32_OperatingSystem(["Caption", "Version"]):
				osversion.print_and_log(log, f"   - {PC_name}")
				csv_out.write(f"{'My PC' if debug else PC_name}, {os_info.Caption}, {os_info.Version}\n")

	def log(file, item):
		"""Writes a line in the log.log file
		"""
		file.write(f"{item}\n")

	def print_and_log(file, item):
		"""Writes on the screen and in the log file
		"""
		print(item)
		osversion.log(file, item)

	def init_csv(init, end, log):
		"""Init the csv files
		"""
		end.write("PC_name, OS, OS_version\n")
		osversion.log(log, "csv now initialized")


if __name__ == "__main__":
	# debug flag
	debug = False

	osversion(debug)
