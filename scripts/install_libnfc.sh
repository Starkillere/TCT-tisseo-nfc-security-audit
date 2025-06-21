#!/bin/bash

echo "[+] Installation des outils NFC..."

sudo apt update
sudo apt install -y libnfc-bin mfoc mfcuk git

echo "[+] Configuration du fichier libnfc"

mkdir -p ~/.config/libnfc
cat <<EOF > ~/.config/libnfc/libnfc.conf
device.name = "ACR122U NFC Reader"
device.connstring = "pn532_usb:001:004"
allow_autoscan = true
EOF

echo "[+] Installation terminée."