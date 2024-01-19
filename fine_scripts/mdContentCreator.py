
import re

#[PKIXCertPathBuilderResult verifyCertificate(X509Certificate cert, Set<X509Certificate> trustedRootCerts, Set<X509Certificate> intermediateCerts)]
#(#pkixcertpathbuilderresult-verifycertificatex509certificate-cert-setx509certificate-trustedrootcerts-setx509certificate-intermediatecerts)

with open("/home/jakub/Work/common-crypto/README.md", mode="r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")

for line in lines:
    if (line.startswith("#")):
        parts = line.split(" ")
        header = parts[0]
        name = " ".join(parts[1:])
        href = []
        for h in parts[1:]:
            h = h.lower()
            h = re.sub('[^0-9a-zA-Z]+', '', h)
            href.append(h)
        
        href = "-".join(href)

        for i in range(2, len(header)):
            print("\t", end="")
        print(f"- [{name}](#{href})")