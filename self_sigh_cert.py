from OpenSSL import crypto, SSL

# https://stackoverflow.com/questions/27164354/create-a-self-signed-x509-certificate-in-python
def cert_gen(commonName="assignment.local",
             serialNumber=0,
             validityStartInSeconds=0,
             validityEndInSeconds=10 * 365 * 24 * 60 * 60,
             KEY_FILE="private.key",
             CERT_FILE="selfsigned.crt"):

    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)

    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().CN = commonName
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')

    with open(CERT_FILE, "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))

    with open(KEY_FILE, "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))


if __name__ == '__main__':
    cert_gen()
