from PIL import Image
import os

# ── ANSI Colors ───────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
DIM     = "\033[2m"
BLUE    = "\033[94m"
# ──────────────────────────────────────────────────────────

# ── Settings ──────────────────────────────────────────────
INPUT_FOLDER  = "input"
OUTPUT_FOLDER = os.path.join("output", "images")

SIZES = {
    "mobile":  480,
    "tablet":  768,
    "desktop": 1440,
}

SUPPORTED = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")
# ──────────────────────────────────────────────────────────


def resize_image(img, width):
    """Resize image to given width, keep aspect ratio."""
    original_width, original_height = img.size
    ratio  = width / original_width
    height = int(original_height * ratio)
    return img.resize((width, height), Image.LANCZOS)


def print_header():
    print(f"\n{BOLD}{CYAN}┌─────────────────────────────┐{RESET}")
    print(f"{BOLD}{CYAN}│         imgkit v1.0         │{RESET}")
    print(f"{BOLD}{CYAN}│  responsive image processor │{RESET}")
    print(f"{BOLD}{CYAN}└─────────────────────────────┘{RESET}\n")


def print_divider():
    print(f"{DIM}─────────────────────────────────{RESET}")


def process_images():
    print_header()

    # Make sure output/images folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Collect supported images from input folder
    images = sorted([
        f for f in os.listdir(INPUT_FOLDER)
        if f.lower().endswith(SUPPORTED)
    ])

    if not images:
        print(f"  {YELLOW}⚠  No images found in the input/ folder.{RESET}")
        print(f"  {DIM}Drop your images in and run again.{RESET}\n")
        return

    print(f"  {WHITE}{BOLD}Found {len(images)} image(s). Starting...{RESET}\n")
    print_divider()

    for index, filename in enumerate(images, start=1):
        input_path = os.path.join(INPUT_FOLDER, filename)

        print(f"\n  {BLUE}{BOLD}[{index}/{len(images)}]{RESET} {WHITE}{filename}{RESET}")

        with Image.open(input_path) as img:
            img = img.convert("RGB")

            for screen, width in SIZES.items():
                resized = resize_image(img, width)

                pad = len(str(len(images)))
                output_name = f"{str(index).zfill(pad)}-{screen}.webp"
                output_path = os.path.join(OUTPUT_FOLDER, output_name)

                resized.save(output_path, format="WEBP", quality=85)
                print(f"       {GREEN}✔{RESET}  {DIM}{screen:<10}{RESET} {WHITE}{output_name}{RESET}")

    print_divider()
    print(f"\n  {GREEN}{BOLD}✔ All done!{RESET}")
    print(f"\n  {YELLOW}{BOLD}Next step:{RESET}")
    print(f"  {WHITE}Copy{RESET} {CYAN}output/images/{RESET} {WHITE}into your project assets.{RESET}")
    print(f"\n  {YELLOW}{BOLD}When finished:{RESET}")
    print(f"  {WHITE}Run{RESET} {CYAN}bash clean.sh{RESET} {WHITE}to clear everything.{RESET}\n")


if __name__ == "__main__":
    process_images()