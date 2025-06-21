#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <fichier_dump_source>"
    exit 1
fi

echo "[*] Écriture sur carte vierge NFC..."
nfc-mfclassic w a "$1" clone_$(date +%s).dmp

if [ $? -eq 0 ]; then
    echo "[+] Clonage réussi."
else
    echo "[!] Échec de l’écriture. UID non modifiable ou erreur matérielle."
fi