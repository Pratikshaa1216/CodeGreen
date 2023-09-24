# CodeGreen - Comparative Analysis of Carbon Footprints in Web Applications

Welcome to CodeGreen! This project is focused on performing a comparative analysis of carbon footprints in web applications.

## Pre-requisites

- Python 3.10 or higher
- Anaconda (if required)
- Docker Desktop (https://www.docker.com/products/docker-desktop/)
- Node.js 
## Development Setup

Clone this repository to your local machine.

### Conda

1. Go to the repository
   ```bash
   cd CodeGreen
   ```

2. Install the required libraries
    ```bash
    conda env create -n codegreen --file requirements.yml
    ```

3. Activate the environment
    ```bash
    conda activate codegreen
    ```

### PIP

1. Go to the repository
   ```bash
   cd CodeGreen
   ```

2. Create a new virtual environment:
    ```bash 
    python -m venv venv --prompt codegreen
    source venv/bin/activate
    ```
    (For Windows)
    ```bash 
    python -m venv codegreen
    cd codegreen/Scripts/activate.bat
    ```

3. Install upgrade some packages
    ```bash
    pip install --upgrade pip setuptools wheel
    ```

4. Install required dependencies
    ```bash
    pip install -r requirements.txt
    ```
### Running python web application

1. **Go to the Script's Directory**: Open a Command Prompt and use the `cd` command to go to the folder where the `app.py` script is located.

   ```bash
   cd /path/to/your/CodeGreen/CodeGreen_Python/app
   ```

2. **Launch the Python Web Application**:
   ```bash
   python app.py
   ```

This command will launch the Python web application.


### Running a JavaScript Web Application

1. **Navigate to the Script's Directory**: Open a Command Prompt and use the `cd` command to change the current directory to the folder where the `index.HTML` script is located.

   ```bash
   cd /path/to/your/JavaScript/CodeGreen/CodeGreen_Javascript
   ```

2. **Launch the JavaScript Web Application**:
   ```bash
   start index.html
   ```

This command will open JavaScript web application.

### Running the Docker Compose File 

If you prefer to use Docker for your development environment, here are the steps to set it up:

1. Install Docker from the official website and ensure that the Docker engine is up and running.

2. Open your terminal and run the following command:
     ```bash
    cd /path/to/your/CodeGreen-main
   ```
  ```bash
   docker compose up -d
   ```

   This will start the necessary containers.

### Accessing the Applications

Once you've completed the setup, you can access the applications as follows:

- **Python Application**: Visit [http://localhost:8050/](http://localhost:8050/) to run the Python application.

- **JavaScript Web Application**: Visit [http://localhost:8080/](http://localhost:8080/) to use the JavaScript web application.


### Running the Web Applications Using Automation Scripts

#### Python Web Application:

1. **Navigate to the Script Directory**: Open a Command Prompt and use the `cd` command to navigate to the directory containing the `auto.py` script.

   ```bash
    cd /path/to/your/CodeGreen/CodeGreen_Python/app
   ```

2. **Execute the Automation Script**: Run the following command to execute the automation script:

   ```bash
   python auto.py
   ```

   This will automatically launch the Python web application.

#### JavaScript Web Application:

1. **Navigate to the Script Directory**: Open a Command Prompt and use the `cd` command to navigate to the directory containing the `autojs.py` script.

   ```bash
   cd /path/to/your/JavaScript/CodeGreen/CodeGreen_Javascript
   ```

2. **Execute the Automation Script**: Run the following command to execute the automation script:

   ```bash
   python autojs.py
   ```

   This will automatically open the JavaScript web application.


