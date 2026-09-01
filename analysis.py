def classify_priority(classification):
    if classification is None:
        return "Low"

    classification = str(classification).strip()

    if classification == "Class I":
        return "Critical"
    if classification == "Class II":
        return "Medium"
    return "Low"
