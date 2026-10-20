
# Bayesian Network.py
# Knowledge Representation using Bayesian Reasoning

def probability_rain(cloudy):
    """Calculate the probability of rain given cloud conditions."""
    if cloudy:
        return 0.8
    return 0.2


def probability_wet_grass(rain, sprinkler):
    """Calculate the probability of wet grass."""
    if rain and sprinkler:
        return 0.99
    elif rain or sprinkler:
        return 0.90
    else:
        return 0.01


def infer_weather(cloudy, sprinkler):
    """Infer the probability of wet grass."""
    p_rain = probability_rain(cloudy)

    p_wet_if_rain = probability_wet_grass(True, sprinkler)
    p_wet_if_no_rain = probability_wet_grass(False, sprinkler)

    p_wet = (
        p_wet_if_rain * p_rain
        + p_wet_if_no_rain * (1 - p_rain)
    )

    return p_rain, p_wet


# Main program
print("=== Bayesian Network ===")
print("Knowledge Representation using Probability\n")

cloudy = input("Is it cloudy? (yes/no): ").strip().lower()
sprinkler = input("Is the sprinkler on? (yes/no): ").strip().lower()

if cloudy not in ("yes", "no") or sprinkler not in ("yes", "no"):
    print("Invalid input! Please enter yes or no.")
else:
    p_rain, p_wet = infer_weather(
        cloudy == "yes",
        sprinkler == "yes"
    )

    print("\n--- Inference Results ---")
    print(f"Probability of rain: {p_rain * 100:.2f}%")
    print(f"Probability of wet grass: {p_wet * 100:.2f}%")

    if p_wet >= 0.5:
        print("Conclusion: Grass is likely to be wet.")
    else:
        print("Conclusion: Grass is unlikely to be wet.")
