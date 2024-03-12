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

## Examples : 

| Task | Command | Origin picture | edited picture |
|------|---------|:--------------:|:--------------:|
|Removing white background *(all pixels with value 255, 255, 255)*|`python main.py -f undraw.png -o out.png -rv 255 -gv 255 -bv 255`|<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/35a33dc1-858a-46ed-8c7d-09402d720935" alt="Undraw icon to demonstrate usage">|<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/87db81d8-5e49-458b-b792-2b54fff78367" alt="Undraw icon to demonstrate usage">|
| task | Command | pic input | pic output |


