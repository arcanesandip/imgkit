# imgkit

Process images into responsive sizes and WebP format.

Built with Python — keeping it simple, readable, and a good way to learn by doing.

---

## Problem

Most image converters are bloated with options you'll never use, and they only handle one image at a time. When you're working on a web project, you just need to drop in your images and get them back as **mobile, tablet, and desktop sizes** plus **WebP format** — nothing more, nothing less.

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
pip install Pillow
```

## Run

```bash
python process.py
```

---

## Requirements

- Python 3.x
- Pillow

---

Supported input formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`