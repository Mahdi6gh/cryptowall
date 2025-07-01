from Crypto.PublicKey import RSA
def do():
    key=RSA.generate(2048)
    privet_key=key.export_key()
    with open("private.pem", "wb") as f:
        f.write(privet_key)   
    public_key=key.publickey().export_key()
    with open("publick.pem", "wb") as f:
        f.write(public_key)
    print("✅ RSA keys created and saved")
