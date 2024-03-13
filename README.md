# pixedit
> Remove some pixel to make transparent background using PIL

Requirements: 
- `Pillow` version 1.1.7

## Usage
Installing environment :
```bash
python3 -m venv .env # Creating virtual environement
source .env/bin/activate # Activating the environment
python -m pip install pillow # Installing the library
```

Running program :
```bash
# To remove all pixels matching the given rgb values :
python main.py -f input.jpg -o output.png -rv 255 -gv 255 -bv 255

# To keep all pixels matching the given rgb values :
python main.py -f input.jpg -o output.png -rv 255 -gv 255 -bv 255 --keep-pixel
```

## Examples : 


|              | Removing pixels | Keeping only selected pixels |
|--------------|:---------------:|:----------------------------:|
| Description  |Removing white background *(all pixels with value 255, 255, 255)*|Keeping only white pixels|
| Command line |`python main.py -f undraw.png -o out.png -rv 255 -gv 255 -bv 255`|`python main.py -f undraw.png -o white.png -rv 255 -gv 255 -bv 255 --keep-pixel`|
| Input image  |<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/35a33dc1-858a-46ed-8c7d-09402d720935" alt="Undraw icon to demonstrate usage">|<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/35a33dc1-858a-46ed-8c7d-09402d720935" alt="Undraw icon to demonstrate usage">|
| Ouput image  |<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/87db81d8-5e49-458b-b792-2b54fff78367" alt="Undraw icon to demonstrate usage">|<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/d6ec741a-1985-4b11-8f94-572bc9828520" alt="Undraw icon to demonstrate usage">|

<!--
<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/3c3d4726-3ec3-4626-9786-573017d0c1f6" alt="Undraw icon to demonstrate usage">|
-->

```bash
usage: Pixedit [-h] -f FILE -o OUT [--keep-pixel] [-rv R_VALUE] [-gv G_VALUE] [-bv B_VALUE] [-d]

Pixel Editor

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input image path
  -o OUT, --out OUT     Output image path
  --keep-pixel          Keep only pixel matching given rgb. By default, it remove all matching rgb pixels
  -rv R_VALUE, --red-value R_VALUE
                        (r,g,b) Red value to remove 0 - 255
  -gv G_VALUE, --green-value G_VALUE
                        (r,g,b) Blue value to remove 0 - 255
  -bv B_VALUE, --blue-value B_VALUE
                        (r,g,b) Green value to remove 0 - 255
  -d, --debug           Enable debug ouput, disabled by default
```

|              | Removing pixels | Keeping only selected pixels |
|--------------|:---------------:|:----------------------------:|
| Description  |Removing only dark cat pixels|Keeping only dark cat pixels|
| Command line |`python main.py --file undraw_cat.png --out out.png -rv 63 -gv 61 -bv 86`|` python main.py --file undraw_cat.png --out out.png -rv 63 -gv 61 -bv 86 --keep-pixel`|
| Input image  |<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/63be04dc-72aa-4a06-bcec-760bd04cfa29" alt="Undraw icon to demonstrate usage">|<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/63be04dc-72aa-4a06-bcec-760bd04cfa29" alt="Undraw icon to demonstrate usage">|
| Ouput image  |<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/81a56086-1adc-44cd-98a9-53d0de27f014" alt="Undraw icon to demonstrate usage">|<img width="200px" src="https://github.com/lostsh/pixedit/assets/43549864/df7bf7e6-4cd5-431c-9482-77ae8c63c5b0" alt="Undraw icon to demonstrate usage">|


