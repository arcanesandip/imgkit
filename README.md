# imgkit

Process images into responsive sizes and WebP format.

Built with Python — keeping it simple, readable, and a good way to learn by doing.

---

## Problem

Two real problems with existing image tools:

**1. No bulk processing** — almost every free tool handles one image at a time. Upload, download, repeat. That gets painful fast when you have a folder of images to process.

**2. Option overload** — tools like GIMP, ImageMagick, and Squoosh are powerful but overwhelming. When you just need 3 sizes and WebP, you don't want to configure 20 settings every time.

imgkit solves both — drop a folder of images, run one command, get back everything you need. Nothing more, nothing less.

---

## How it works

1. Drop your images into the `input/` folder
2. Run the script
3. Pick up your processed images from the `output/` folder

---

## Output sizes

| Screen  | Width  |
|---------|--------|
| Mobile  | 480px  |
| Tablet  | 768px  |
| Desktop | 1440px |

Height is auto — aspect ratio is always preserved.

---

## Output naming

Images are numbered in the order they are processed:

```
output/
├── 1-mobile.webp
├── 1-tablet.webp
├── 1-desktop.webp
├── 2-mobile.webp
├── 2-tablet.webp
└── 2-desktop.webp
```

---

## Setup

```bash
# 1. Run setup once
bash setup.sh

# 2. Activate the venv
source venv/bin/activate

# 3. Process your images
python process.py
```

---

## Requirements

- Python 3.x
- Pillow

---

Supported input formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`