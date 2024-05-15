from flask import Flask, Response
import qrcode

app = Flask(__name__)


@app.route("/<data>")
def generate_qr(data):
    # Generate a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an ASCII representation of the QR code
    ascii_qr = []
    for line in qr.get_matrix():
        ascii_line = "".join(["██" if cell else "  " for cell in line])
        ascii_qr.append(ascii_line)

    ascii_qr_text = "\n".join(ascii_qr)

    # Return ASCII QR code as plain text response
    return Response(ascii_qr_text, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
