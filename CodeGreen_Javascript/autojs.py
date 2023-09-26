import subprocess
import time
from codecarbon import EmissionsTracker
import psutil

def start_web_application():
    # Start a web server using the 'http.server' module on port 8080
    subprocess.Popen(["python", "-m", "http.server", "8080"])

def open_browser(url):
    # Open a web browser with the specified URL
    subprocess.Popen(["start", "", url], shell=True)

def track_emissions(duration):

    tracker = EmissionsTracker()
    tracker.start()  # Start tracking emissions


    time.sleep(duration)

    tracker.stop()  # Stop tracking emissions
    tracker.save_to_csv("emissions.csv")  # Save emissions data to a CSV file

def shutdown_web_application():
  for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'python' and '-m http.server 8080' in ' '.join(proc.cmdline()):
            print("Web application process:", proc.info['name'], proc.info['pid'])
            proc.terminate()  

def main():
    duration = 90  # Duration (in seconds) for which to track emissions

    start_web_application()  # Start the web server
    open_browser("http://127.0.0.1:8080/index.html")  # Open the web page in a browser
    track_emissions(duration)  # Track emissions during the specified duration

    shutdown_web_application()  # Shutdown the web server process

if __name__ == '__main__':
    main()  



