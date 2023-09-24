import subprocess
import time
from codecarbon import EmissionsTracker
import psutil

def start_web_application():
   
    subprocess.Popen(["python", "-m", "http.server", "8080"])

def open_browser(url):
   
    subprocess.Popen(["start", "", url], shell=True)

def track_emissions(duration):
    tracker = EmissionsTracker()
    tracker.start()

   
    time.sleep(duration)

    tracker.stop()
    tracker.save_to_csv("emissions.csv")

def shutdown_web_application():
 
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'python' and '-m http.server 8080' in ' '.join(proc.cmdline()):
            print("Web application process:", proc.info['name'], proc.info['pid'])
            proc.terminate()

def main():
    duration = 90 

    start_web_application()
    open_browser("http://127.0.0.1:8080/index.html")  
    track_emissions(duration)

    shutdown_web_application()

if __name__ == '__main__':
    main()


