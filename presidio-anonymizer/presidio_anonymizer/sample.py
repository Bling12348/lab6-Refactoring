from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig
from typing import Optional

def sample_run_anonymizer(
    text: Optional[str] = None,
    person_start: Optional[int] = None,
    person_end: Optional[int] = None
):
    """
    Refactored function to allow testability.

    If parameters are provided, they are used.
    Otherwise, fall back to input().
    """
    engine = AnonymizerEngine()

    if text is None:
        text = input("text: ")
    if person_start is None:
        person_start = int(input("start: "))
    if person_end is None:
        person_end = int(input("end: "))

    analyzer_results = [
        RecognizerResult(
            entity_type="PERSON",
            start=person_start,
            end=person_end,
            score=0.8
        )
    ]

    operators = {"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}

    result = engine.anonymize(
        text=text,
        analyzer_results=analyzer_results,
        operators=operators
    )

    print(result)
    return result

if __name__ == "__main__":
    sample_run_anonymizer()
