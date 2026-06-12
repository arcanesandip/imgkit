from PIL import Image
import os

# ── Settings ──────────────────────────────────────────────
INPUT_FOLDER  = "input"
OUTPUT_FOLDER = "output"

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


def process_images():
    # Make sure output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Collect supported images from input folder
    images = sorted([
        f for f in os.listdir(INPUT_FOLDER)
        if f.lower().endswith(SUPPORTED)
    ])

    if not images:
        print("No images found in the input folder.")
        return

    print(f"Found {len(images)} image(s). Processing...\n")

    for index, filename in enumerate(images, start=1):
        input_path = os.path.join(INPUT_FOLDER, filename)

        with Image.open(input_path) as img:
            # Convert to RGB so WebP/JPEG export works cleanly
            img = img.convert("RGB")

            for screen, width in SIZES.items():
                resized = resize_image(img, width)

                output_name = f"{index}-{screen}.webp"
                output_path = os.path.join(OUTPUT_FOLDER, output_name)

                resized.save(output_path, format="WEBP", quality=85)
                print(f"  ✔ {output_name}")

        print(f"  Done — image {index} of {len(images)}\n")

    print("All images processed. Check the output folder.")


if __name__ == "__main__":
    process_images()