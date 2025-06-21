import subprocess
import time
import statistics
from datetime import datetime

def read_card():
    start = time.time()
    try:
        result = subprocess.run(
            ["nfc-list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3
        )
        success = b"UID" in result.stdout
        duration = time.time() - start
        return success, duration
    except subprocess.TimeoutExpired:
        return False, 3.0

def run_tests(iterations=20, delay=0.5):
    results = []
    for i in range(iterations):
        print(f"[{i+1}/{iterations}] Test en cours...")
        success, duration = read_card()
        results.append((success, duration))
        time.sleep(delay)
    
    return results

def analyze_results(results):
    times = [d for success, d in results if success]
    fails = [1 for success, _ in results if not success]

    print("\n--- Résultats ---")
    print(f"Nombre total d'essais : {len(results)}")
    print(f"Réussites              : {len(times)}")
    print(f"Échecs                 : {len(fails)}")
    
    if times:
        print(f"Temps moyen de lecture : {statistics.mean(times):.3f}s")
        print(f"Temps max              : {max(times):.3f}s")
        print(f"Temps min              : {min(times):.3f}s")
    else:
        print("Aucune lecture réussie")

def save_results(results):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"antenne_resultats_{now}.csv", "w") as f:
        f.write("essai,réussite,durée(s)\n")
        for i, (success, duration) in enumerate(results, 1):
            f.write(f"{i},{int(success)},{duration:.3f}\n")
    print(f"Résultats sauvegardés dans antenne_resultats_{now}.csv")

if __name__ == "__main__":
    print("=== Étude de fiabilité antenne NFC ===")
    tests = run_tests()
    analyze_results(tests)
    save_results(tests)
