# Tower-of-Hanoi
Solving Tower of Hanoi using TensorFlow.

## Testing
Linux:
```bash
virtualenv env
source env/bin/activate
pip install --upgrade .
make test
```

Windows:
```powershell
virtualenv env
.\env\Scripts\activate.ps1
pip install --upgrade .
nosetests --nocapture --with-coverage --cover-package=hanoi
```