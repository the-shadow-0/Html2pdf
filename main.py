# main.py
from fastapi import FastAPI, Request, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil, os, uuid, asyncio
import img2pdf
from pyppeteer import launch

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def ensure_html(filename: str):
    if not filename.lower().endswith(".html"):
        raise HTTPException(400, "Only .html files are allowed")

async def render_highres_png(html_path: str, png_path: str, scale: int = 2):
    browser = await launch({ "args": ["--no-sandbox","--disable-setuid-sandbox"] })
    page = await browser.newPage()
    await page.setViewport({"width":1200,"height":800,"deviceScaleFactor":scale})
    await page.emulateMedia("screen")
    await page.goto(f"file://{os.path.abspath(html_path)}", {"waitUntil":"networkidle0"})
    dims = await page.evaluate(
        "() => { const d = document.documentElement; return { width:d.scrollWidth, height:d.scrollHeight }; }"
    )
    await page.setViewport({"width":dims["width"],"height":dims["height"],"deviceScaleFactor":scale})
    await page.screenshot({"path":png_path,"fullPage":True})
    await browser.close()
    return dims

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert_file")
async def convert_file(format: str = Form(...), file: UploadFile = File(...)):
    ensure_html(file.filename)
    uid = uuid.uuid4().hex
    html_f = os.path.join(UPLOAD_DIR, f"{uid}.html")
    with open(html_f, "wb") as out:
        shutil.copyfileobj(file.file, out)
    png_f = os.path.join(UPLOAD_DIR, f"{uid}.png")
    await render_highres_png(html_f, png_f)
    if format == "image":
        return FileResponse(png_f, media_type="image/png", filename="output.png")
    pdf_f = os.path.join(UPLOAD_DIR, f"{uid}.pdf")
    with open(pdf_f, "wb") as f:
        f.write(img2pdf.convert(png_f, dpi=96))
    return FileResponse(pdf_f, media_type="application/pdf", filename="output.pdf")

@app.post("/convert_code")
async def convert_code(format: str = Form(...), html_code: str = Form(...)):
    uid = uuid.uuid4().hex
    html_f = os.path.join(UPLOAD_DIR, f"{uid}.html")
    with open(html_f, "w", encoding="utf-8") as f:
        f.write(html_code)
    png_f = os.path.join(UPLOAD_DIR, f"{uid}.png")
    await render_highres_png(html_f, png_f)
    if format == "image":
        return FileResponse(png_f, media_type="image/png", filename="output.png")
    pdf_f = os.path.join(UPLOAD_DIR, f"{uid}.pdf")
    with open(pdf_f, "wb") as f:
        f.write(img2pdf.convert(png_f, dpi=96))
    return FileResponse(pdf_f, media_type="application/pdf", filename="output.pdf")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
