import qrcode
data = input("Enter the text or URL to generate QR code: ").strip()
filename = input("Enter the filename: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code generated and saved as {filename}")

# To create a virtual environment:
# 1. Open your terminal 
# 2. python -m venv venv(second venv chai name ho venv ko we can change it to any name such as myvenv)
# 3. Activate the virtual environment:
#    - On Windows: venv\Scripts\activate
# 4. Install the required packages:
#     - pip install qrcode
#     -pip install pillow
# 5. Run the script:
#    - python qr_code_generator.py

# To deactivate the virtual environment, simply type `deactivate` in the terminal.