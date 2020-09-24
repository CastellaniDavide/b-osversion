# osversion
[![GitHub license](https://img.shields.io/badge/licence-GNU-green?style=flat)](https://github.com/CastellaniDavide/cpp-osversion/blob/master/LICENSE) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v01.02-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/osversion)

## Description
Get the os vesioning by a list of PC.
The output will be printed in "osversion.csv" file & "osversion.db" database

## Required
 - python3
 - pip3 packages (in the repo core pip3 install -r requirements/requirements.txt)
 
## Directories structure
 - .github
   - ISSUE_TEMPLATE
     - bug_report.md
     - feature-request.md
 - bin
   - **osversion.py**
 - docs
   - LICENSE
   - README.md
 - flussi
   - computers.csv
   - osversion.csv
   - osversion.db
 - log
   - trace.log
 - requirements
   - requirements.txt
   
### Execution examples (in bin folder)
 - python3 osversion.py

# Changelog
 - [Version_01.02_2020-9-24](#Version_0102_2020-9-24)
 - [Version_01.01_2020-9-18](#Version_0101_2020-9-18)

## Version_01.02_2020-9-24
 - Added an optimization in csv write: helps to prevent some problems

## Version_01.01_2020-9-18
 - Initial version

---
Made by Castellani Davide 
If you have any problem please contact me:
- help@castellanidavide.it
- [Issue](https://github.com/CastellaniDavide/osversion/issues)
