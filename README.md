# boring-python

A really small collection of boring python scripts, maybe some day I'll add another boring script.

Feel free to use any code for any purpose. I don't judge.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/robinhickmann/boring-python.git
    cd boring-python
    ```

2. Create a python virtual envrionment
   
- On macOS/Linux
    ```bash
    python3 -m venv venv 
    ```

- On Windows
    ```bash
    python -m venv venv
    ```

3. Activate the virtual envrionment

- On macOS/Linux
    ```bash
    source venv/bin/activate
    ```

- On Windows
    ```bash
    # In cmd.exe
    venv\Scripts\activate.bat
    # In PowerShell
    venv\Scripts\Activate.ps1
    ```

4. Download and install dependencies

    Also make sure you have tkinter installed on your system.

- On macOS/Linux
    ```bash
    pip3 install -r requirements.txt
    ```

- On Windows
    ```bash
    pip install -r requirements.txt
    ```

5. Run whichever script you want

- On macOS/Linux
    ```bash
    python3 path/to/file
    ```

- On Windows
    ```bash
    python path/to/file
    ```

#### If you want to exit and remove the virtual environment

1. Exit the virtual envrionment
    ```bash
    deactivate
    ```

2. Remove the virtual envrionment
    ```bash
    rm -rf venv
    ```

## License

All code in this repo is licensed under MIT.
