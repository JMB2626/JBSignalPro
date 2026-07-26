import csv
import os

FILE = "history.csv"

def save_signal(ema20, ema50, ema200, rsi, signal, prix_entree):
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "ema20",
                "ema50",
                "ema200",
                "rsi",
                "signal",
                "entry",
                "result"
            ])

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            ema20,
            ema50,
            ema200,
            rsi,
            signal,
            prix_entree,
            -1
        ])
