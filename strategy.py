from history import save_signal


def analyse(df):

    if len(df) < 20:
        return "⏸ ATTENTE", 50

    # Dernières bougies
    current = df.iloc[-1]
    previous = df.iloc[-2]

    # Recherche du dernier Swing High et Swing Low
    swing_high = df["high"].iloc[-10:-2].max()
    swing_low = df["low"].iloc[-10:-2].min()

    score_buy = 0
    score_sell = 0

    # =========================
    # BOS (Break Of Structure)
    # =========================

    if current["close"] > swing_high:
        score_buy += 40

    if current["close"] < swing_low:
        score_sell += 40


    # =========================
    # CHOCH (changement structure)
    # =========================

    if previous["close"] < previous["open"] and current["close"] > current["open"]:
        score_buy += 20

    if previous["close"] > previous["open"] and current["close"] < current["open"]:
        score_sell += 20


    # =========================
    # Retest du niveau cassé
    # =========================

    if current["low"] <= swing_high and current["close"] > swing_high:
        score_buy += 20

    if current["high"] >= swing_low and current["close"] < swing_low:
        score_sell += 20


    # =========================
    # Volume confirmation
    # =========================

    if "volume" in df.columns:

        volume_moyen = df["volume"].iloc[-10:].mean()

        if current["volume"] > volume_moyen:
            if score_buy > score_sell:
                score_buy += 20
            elif score_sell > score_buy:
                score_sell += 20
                trend_up = df["close"].iloc[-20] < df["close"].iloc[-1]
                trend_down = df["close"].iloc[-20] > df["close"].iloc[-1]


    # =========================
    # Décision finale
    # =========================

    if trend_up and score_buy >= 70:
        save_signal(
            0,
            0,
            0,
            0,
            "BUY",
            current["close"]
        )
        return "🟢 ACHAT", score_buy


    if trend_down and score_sell >= 70:
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
