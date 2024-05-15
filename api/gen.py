from flask import Flask, Response, request
import qrcode

app = Flask(__name__)


@app.route("/", methods=["GET"])
def generate_qr():
    data = request.args.get("data", "")

    # Generate a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=0,  # Set border to 0 to avoid additional margins
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an ASCII representation of the QR code
    qr_matrix = qr.get_matrix()

    ascii_qr = []
    for line in qr_matrix:
        ascii_line = "".join(["██" if cell else "  " for cell in line])
        ascii_qr.append(ascii_line)

    ascii_qr_text = "\n".join(ascii_qr)

    # Return ASCII QR code as plain text response
    return Response(ascii_qr_text, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
