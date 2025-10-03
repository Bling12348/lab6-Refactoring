from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    start = 11
    end = 15

    result = sample_run_anonymizer(text=text, person_start=start, person_end=end)

    assert result.text == "My name is BIP."

    first_item = result.items[0]
    assert first_item['start'] == start
    assert first_item['end'] == end - 1  # Presidio uses end-1 indexing
    assert first_item['entity_type'] == "PERSON"
    assert first_item['text'] == "BIP"
    assert first_item['operator'] == "replace"
