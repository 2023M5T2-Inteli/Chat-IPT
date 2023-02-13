## How to create a venv (not necessary to run)
Run this code on the root of the folder that you want to create the venv
On mac:
```bash
python3 -m venv .env
```
On windows:
```bash
py -m venv .env
```
## For activating the venv
Run this code in your terminal in the root of this folder.
For mac:
```bash
source env/bin/activate
```
For windows:
```bash
.\env\Scripts\activate
```
To leave the venv run:
```bash
deactivate
```
## For installing the libraries from the requirements.txt
Run this code on the root of this folder:
```bash
pip install -r requirements.txt
```

## For exporting the libraries that were installed in this venv
Run this code on the root of this folder:
```bash
pip freeze --> requirements.txt
```