# pixedit
> Remove some pixel to make transparent background using PIL

Requirements: 
- `Pillow` version 1.1.7

## Usage
Installing environment :
```bash
python3 -m venv .env
source .env/bin/activate
python -m pip install pillow
```

Running program :
```bash
python main.py -f input.jpg -o output.png --remove-r 255 --remove-g 255 --remove-b 255
```