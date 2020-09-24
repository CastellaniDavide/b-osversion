"""osversion
"""
import os, wmi, sqlite3
from datetime import datetime

__author__ = "help@castellanidavide.it"
__version__ = "01.02 2020-9-18"

class osversion:
	def __init__ (self, debug=False):
		"""The core of my project
		"""
		base_dir = "." if debug else ".." # the project "root" in Visual studio it is different

		# Open files
		log = open(os.path.join(base_dir, "log", "trace.log"), "a")
		csv_in = open(os.path.join(base_dir, "flussi", "computers.csv"), "r")
		csv_out = open(os.path.join(base_dir, "flussi", "osversion.csv"), "w+")
		db_osversion = sqlite3.connect(os.path.join(base_dir, "flussi", "osversion.db")).cursor()

		osversion.log(log, "Opened all files and database connected")
		
		# Start time
		start_time = datetime.now()
		osversion.log(log, f"Start time: {start_time}")
		osversion.log(log, "Running: osversion.py")

		# Init files and db
		intestation = "PC_name, OS, OS_version"
		osversion.init_csv(csv_in, csv_out, intestation, log)
		osversion.init_db(db_osversion, intestation, log)

		# Core operations
		osversion.print_OS_Info(log, csv_in, csv_out, db_osversion, debug)

		# Check db
		osversion.check_db(db_osversion, intestation, log)

		# End
		osversion.log(log, f"End time: {datetime.now()}\nTotal time: {datetime.now() - start_time}")
		osversion.log(log, "")
		log.close()
		csv_in.close()
		csv_out.close()

	def print_OS_Info(log, csv_in, csv_out, db_osversion, debug):
		"""Prints the infos by Win32_OperatingSystem
		"""
		osversion.print_and_log(log, " - Get OS and OS version in:")
		
		# Only on the PC if debug is true, else on all PCs in the list
		for PC_name in ("My PC, debug option",) if debug else csv_in.read().split("\n")[1:]:
			# Establish a new connection
			conn = wmi.WMI("." if debug else PC_name)

			# Get the necessary infos
			for os_info in conn.Win32_OperatingSystem(["Caption", "Version"]):
				osversion.print_and_log(log, f"   - {PC_name}")
				data = f"'{'My PC' if debug else PC_name}','{os_info.Caption}','{os_info.Version}'"
				csv_out.write(f"""{osversion.make_csv_standart(data).replace("'", '"')}\n""")
				db_osversion.execute(f"INSERT INTO osversion VALUES ({data})")

	def make_csv_standart(data):
		"""Convert my text in csv standard to prevent errors
		Reference: https://tools.ietf.org/html/rfc4180
		"""
		data.replace(",", "%x2C").replace("}%x2C{", "},{")	# make sure extra commas
		data.replace("\"", "%x22").replace("%x22", "\"", 1).replace("%x22", "\"") # make sure extra double commas
		data.replace("'", '"') # Use " and not ', as csv standard
		data.encode("ASCII")
		return data

	def log(file, item):
		"""Writes a line in the log.log file
		"""
		file.write(f"{item}\n")

	def print_and_log(file, item):
		"""Writes on the screen and in the log file
		"""
		print(item)
		osversion.log(file, item)

	def init_csv(init, end, intestation, log):
		"""Init the csv files
		"""
		end.write(f"{intestation}\n")
		osversion.log(log, "csv now initialized")

	def init_db(db_osversion, intestation, log):
		"""Init the database
		"""
		try:
			db_osversion.execute(f'''CREATE TABLE osversion ({intestation})''')
		except:
			db_osversion.execute("DROP TABLE osversion")
			db_osversion.execute(f'''CREATE TABLE osversion ({intestation})''')

		osversion.log(log, "database now initialized")

	def check_db(db_file, intestation, log, tablename="osversion"):
		"""Checks the database content
		"""
		print("\nDatabase content:")
		print(f"{intestation}")

		for row in db_file.execute(f"SELECT * FROM {tablename}"):
			print(str(row)[1:-1].replace("'", ""))

if __name__ == "__main__":
	# debug flag
	debug = False

	osversion(debug)
