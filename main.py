## Author : Vernhes Yohann - lostsh

from sys import argv, stderr, stdin
import argparse
from PIL import Image

def remove_pix_value(file, pix_to_remove=(0, 0, 0)):
    base_img = Image.open(file)
    largeur, hauteur = base_img.size
    out_img = Image.new("RGBA", (largeur, hauteur))
    for y in range(0, hauteur):
        for x in range(0, largeur):
            current_col = base_img.getpixel((x, y))
            current_col = current_col
            if(current_col[:3] == pix_to_remove):
                current_col = (255, 255, 255, 0)
            out_img.putpixel((x, y), current_col)
    return out_img


def main(input_file: str, output_file: str, rgb_to_remove: tuple) -> None:
    print("\t[>] Run main.")
    print("\t[;] Debug rgb value to remove: ", rgb_to_remove)
    remove_pix_value(input_file, rgb_to_remove).save(output_file, 'png')
    print("\t[<] End main.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Pixedit",
        description="Pixel Editor"
    )
    parser.add_argument('-f', '--file', type=str, help="Input image path", required=True)
    parser.add_argument('-o', '--out', type=str, help="Output image path", required=True)
    parser.add_argument('--remove-red', dest='r_value', type=int, default=0, 
                        help="(r,g,b) Red value to remove 0 - 255")
    parser.add_argument('--remove-green', dest='g_value', type=int, default=0, 
                        help="(r,g,b) Blue value to remove 0 - 255")
    parser.add_argument('--remove-blue', dest='b_value', type=int, default=0, 
                        help="(r,g,b) Green value to remove 0 - 255")

    args = parser.parse_args()

    # checking if input is from pipe
    if not stdin.isatty():
        print("\t[!] Cannot pipe input", file=stderr)
        parser.print_help()
        exit(1)

    # check valid args number
    if(len(argv) < 1):
        print("\t[!] Missing arguments", file=stderr)
        parser.print_help()
        exit(1)
    
    
    
    print("\t[+] Reading from **args")

    main(input_file=args.file, output_file=args.out, rgb_to_remove=(args.r_value, args.g_value, args.b_value))
    
    print("\t[*] Exit")