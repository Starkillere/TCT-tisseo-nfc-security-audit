# TCT-tisseo-nfc-security-audit
## Audit de sécurité NFC – Réseau Tisséo

**Auteur** : A.Anrezki  
**Objectif** : Évaluer la sécurité des cartes de transport NFC utilisées par le réseau Tisséo (Toulouse), dans le cadre d'un audit technique légal.

---

## 📌 Objectifs du projet

- Identifier le type de puces utilisées (MIFARE Classic, DESFire, etc.)
- Analyser les protections logiques (authentification, chiffrement)
- Tester la résistance aux outils open-source (mfoc, libnfc, mfcuk)
- Évaluer les risques de clonage, duplication ou manipulation

---

## 🧰 Outils utilisés

- `libnfc`
- `mfoc`
- `mfcuk`
- `nfc-mfclassic`
- `TagInfo by NXP` (mobile)
- `ACR122U` (lecteur NFC)

---

## 📁 Structure

- `scripts/` : Scripts shell pour automatiser lecture, brute-force, clonage
- `dumps/` : Dumps hexadécimaux des cartes (anonymisés)
- `notes/` : Documentation technique

---

## ⚠️ Disclaimer

Ce dépôt est strictement réservé à un usage légal et éthique.  
Il ne constitue en aucun cas une incitation à cloner, pirater ou falsifier des titres de transport.

---

## 📄 Licence

[MIT License](LICENSE)
