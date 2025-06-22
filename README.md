# HTML to PDF/Image Converter

![convert_1](https://github.com/user-attachments/assets/6897e3d3-d413-4930-8895-87caa7af5b9a)

![convert_2](https://github.com/user-attachments/assets/5581496e-8e5f-41ed-b334-3bec611d5575)

## A sleek, modern web application built with FastAPI that lets you:

   Upload an HTML file (validated for .html extension)

   Edit HTML directly via an in‑browser code editor

   Convert your HTML to a high‑resolution PNG screenshot or a PDF

   Download the result instantly, with pixel‑perfect fidelity

The UI is styled with Tailwind CSS, enhanced by gradients, shadows, and icons from Heroicons, and features the Ace Editor for a smooth coding experience. 

## 🚀 Features

   Two conversion modes

   File Upload: Choose an existing .html file

   Code Editor: Write or paste HTML directly in the browser

   High‑res rendering using Pyppeteer (headless Chromium)

   Single‑page PDF or full‑page PNG output at 2× device‑pixel ratio

   Responsive, modern UI with Tailwind CSS & Heroicons

   Zero‑JavaScript frameworks—just vanilla JS for form handling

## 🔧 Installation

  Clone the repo

    git clone https://github.com/github.com/the-shadow-0/Html2pdf.git
    cd Html2pdf

  Create & activate a virtual environment

    python3 -m venv .venv
    source .venv/bin/activate

  Install Python dependencies

    pip install -r requirements.txt

  Install system prerequisites

    Chromium (for Pyppeteer)
    On Ubuntu/Debian:

        sudo apt-get update
        sudo apt-get install -y chromium-browser

        (Windows/Mac: Pyppeteer will auto‑download Chromium on first run.)

## ▶️ Running Locally

    uvicorn main:app --reload

Navigate to http://localhost:8000 in your browser. You’ll see the converter UI—try uploading an HTML or writing code, select PDF or PNG, and click Convert!
## 🛠️ Usage

  Upload File tab

        Click Select HTML File and pick a .html from your machine.

        Choose PDF or PNG.

        Hit Convert—your browser will download output.pdf or output.png.

    Code Editor tab

        Write or paste HTML in the dark‑mode Ace Editor.

        Select PDF or PNG from the dropdown.

        Click Run & Download.

## 📦 Dependencies

    FastAPI & Uvicorn for the web server

    Jinja2 for templating

    Pyppeteer for headless Chromium rendering

    img2pdf for PNG → PDF conversion

    Tailwind CSS (via CDN) for styling

    Ace Editor for in‑browser HTML editing

    Heroicons (via iconify-icon) for UI icons

See requirements.txt for exact versions.

## 🙌 Contributing

    Fork the repository

    Create a new branch: git checkout -b feature/my-feature

    Commit your changes & push: git push origin feature/my-feature

    Open a Pull Request

## 📝 License

This project is licensed under the MIT License.
