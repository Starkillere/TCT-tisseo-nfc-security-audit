#!/bin/bash

DICT="tools/dictionnaire-cles-mifare.txt"
OUTPUT="dumps/bruteforce_$(date +%s).dmp"

echo "[*] Brute-force avec mfoc - dictionnaire : $DICT"
mfoc -f "$DICT" -O "$OUTPUT"

if [ $? -eq 0 ]; then
    echo "[+] Dump bruteforcé : $OUTPUT"
else
    echo "[!] Aucune clé trouvée avec ce dictionnaire."
fi