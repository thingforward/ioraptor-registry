# Create a downloader
$downloader = New-Object System.Net.WebClient

# Download and install Python 2.7
$downloader.DownloadFile("https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi", "$pwd\python-2.7.14.msi")

# Start Python installation and wait for finish
& start-process .\python-2.7.14.msi -wait

# Get PlatformIO installer script
$downloader.DownloadFile("https://raw.githubusercontent.com/platformio/platformio/develop/scripts/get-platformio.py", "$pwd\get-platformio.py")

#Start PlatformIO installation
& "python" .\get-platformio.py