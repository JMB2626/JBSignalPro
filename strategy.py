from history import save_signal
from structure import trend


def analyse(df):

    if len(df) < 20:
        return "⏸ ATTENTE", 50

    current = df.iloc[-1]
    previous = df.iloc[-2]

    direction = trend(df)
    swing_high = df["high"].iloc[-10:-2].max()
    swing_low = df["low"].iloc[-10:-2].min()

    score_buy = 0
    score_sell = 0

    # =========================
    # BOS
    # =========================

    if current["close"] > swing_high:
        score_buy += 40

    if current["close"] < swing_low:
        score_sell += 40

    # =========================
    # CHOCH
    # =========================

    if previous["close"] < previous["open"] and current["close"] > current["open"]:
        score_buy += 20

    if previous["close"] > previous["open"] and current["close"] < current["open"]:
        score_sell += 20

    # =========================
    # RETEST
    # =========================

    if current["low"] <= swing_high and current["close"] > swing_high:
        score_buy += 20

    if current["high"] >= swing_low and current["close"] < swing_low:
        score_sell += 20

    # =========================
    # Confirmation par le volume
    # =========================

    if "volume" in df.columns:

        volume_moyen = df["volume"].iloc[-10:].mean()

        if current["volume"] > volume_moyen:

            if score_buy > score_sell:
                score_buy += 20

            elif score_sell > score_buy:
                score_sell += 20

    # =========================
    # Filtre de tendance
    # =========================

    

    # =========================
    # Décision finale
    # =========================

    if direction == "UP" and score_buy >= 70:

        save_signal(
            0,
            0,
            0,
            0,
            "BUY",
            current["close"]
        )

        return "🟢 ACHAT", score_buy

    if direction == "DOWN" and score_sell >= 70:

        save_signal(
            0,
            0,
            0,
            0,
            "SELL",
            current["close"]
        )

        return "🔴 VENTE", score_sell

    return "⏸ ATTENTE", max(score_buy, score_sell)
