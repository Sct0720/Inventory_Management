## Create and activate Python virtual environment
```bash
    python -m venv venv
    venv/Scripts/activate
```

## Install dependencies
Create file *requirements.txt*

```bash
    pip3 install -r requirements.txt
```

## Run uvicorn project

```bash
    uvicorn main:app --reload 
```


# Utilities
## Steps to remove virtual environment
```bash
    deactivate
    rm -rf venv
```
