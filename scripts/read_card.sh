#!/bin/bash

OUTPUT_FILE="dumps/carte_$(date +%s).dmp"
echo "[*] Lecture de la carte NFC avec mfoc..."
mfoc -O "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "[+] Dump réussi : $OUTPUT_FILE"
else
    echo "[!] Échec de la lecture. Carte protégée ou non compatible."
fi