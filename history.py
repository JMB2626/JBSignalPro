import csv
import os
import time

FILE = "history.csv"

def save_signal(ema20, ema50, ema200, rsi, signal, entry, result=-1):

    existe = os.path.exists(FILE)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not existe:
            writer.writerow([
                "time",
                "ema20",
                "ema50",
                "ema200",
                "rsi",
                "signal",
                "entry",
                "result"
            ])

        writer.writerow([
            int(time.time()),
            ema20,
            ema50,
            ema200,
            rsi,
            signal,
            entry,
            result
        ])
