import subprocess
import time
from codecarbon import EmissionsTracker
import psutil

def start_web_application():
    # Start a simple web server to serve the "index.html" file on port 8080
    subprocess.Popen(["python", "-m", "http.server", "8080"])

def open_browser(url):
    # Open the default web browser with the specified URL on Windows
    subprocess.Popen(["start", "", url], shell=True)

def track_emissions(duration):
    tracker = EmissionsTracker()
    tracker.start()

    # Track emissions for the specified duration (in seconds)
    time.sleep(duration)

    tracker.stop()
    tracker.save_to_csv("emissions.csv")

def shutdown_web_application():
    # Find the Python process running the web server on port 8080 and terminate it
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'python' and '-m http.server 8080' in ' '.join(proc.cmdline()):
            print("Web application process:", proc.info['name'], proc.info['pid'])
            proc.terminate()

def main():
    duration = 90  # Duration in seconds before shutting down the website

    start_web_application()
    open_browser("http://127.0.0.1:8080/index.html")  # Include "/index.html"
    track_emissions(duration)

    shutdown_web_application()

if __name__ == '__main__':
    main()


