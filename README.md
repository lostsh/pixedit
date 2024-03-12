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
# To remove all pixels matching the given rgb values :
python main.py -f input.jpg -o output.png -rv 255 -gv 255 -bv 255

# To keep all pixels matching the given rgb values :
python main.py -f input.jpg -o output.png -rv 255 -gv 255 -bv 255 --keep-pixel
```