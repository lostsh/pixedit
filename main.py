## Author : Vernhes Yohann - lostsh

from sys import argv, stderr, stdin
import argparse
from PIL import Image

# Global debug flag
DEBUG = False

# Main function, remove or keep pixel matching given rgb
def apply_change_to_pixel(file, pix_value=(0, 0, 0), remove_pix=True):
    base_img = Image.open(file)
    largeur, hauteur = base_img.size
    out_img = Image.new("RGBA", (largeur, hauteur))
    if(DEBUG): print("\t[@] Debug: ", end='')
    for y in range(0, hauteur):
        for x in range(0, largeur):
            current_col = base_img.getpixel((x, y))
            current_col = current_col
            if(DEBUG and y%32==0 and x%32==0): print(current_col, end=' ')
            if( (remove_pix and current_col[:3] == pix_value) or ( not(remove_pix) and current_col[:3] != pix_value)):
                current_col = (255, 255, 255, 0)
            out_img.putpixel((x, y), current_col)
    if(DEBUG): print("")
    return out_img


def main(input_file: str, output_file: str, rgb_value: tuple, remove_pixel: bool) -> None:
    print("\t[>] Run main.")
    apply_change_to_pixel(input_file, rgb_value, remove_pixel).save(output_file, 'png')
    print("\t[<] End main.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Pixedit",
        description="Pixel Editor"
    )
    parser.add_argument('-f', '--file', type=str, help="Input image path", required=True)
    parser.add_argument('-o', '--out', type=str, help="Output image path", required=True)
    parser.add_argument('--keep-pixel', dest='keep_pix', action='store_true', default=False, 
                        help="Keep only pixel matching given rgb. By default, it remove all matching rgb pixels")
    parser.add_argument('-rv', '--red-value', dest='r_value', type=int, default=0, 
                        help="(r,g,b) Red value to remove 0 - 255")
    parser.add_argument('-gv', '--green-value', dest='g_value', type=int, default=0, 
                        help="(r,g,b) Blue value to remove 0 - 255")
    parser.add_argument('-bv', '--blue-value', dest='b_value', type=int, default=0, 
                        help="(r,g,b) Green value to remove 0 - 255")
    parser.add_argument('-d', '--debug', dest='debug', action='store_true', default=False,
                        help="Enable debug ouput, disabled by default")

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

    #print("\t[;] Debug for remove pixel bool value: ", args.keep_pix)
    DEBUG = args.debug
    if(DEBUG): print("\t[@] Debug enabled.")
    main(input_file=args.file, output_file=args.out, rgb_value=(args.r_value, args.g_value, args.b_value), remove_pixel=not(args.keep_pix))

    print("\t[*] Exit")