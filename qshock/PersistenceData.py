
class ShockPatientSummary:

    subject_id = None
    shock_date = None
    pressor_events = []

    MAP_measurements = []

    culture_sampling_events = []

    antibiotics_administration_events = []

    lactate_measurements = []

    creatinine_measurements = []
    total_daily_fluid_administration = []
    codes = [] #ICD9/10 and SNOMED problem list

    discharge_summary = None

    all_measurements_text = None

    def __init__(self):
        return

class SingleMeasurement:

    datetime = None
    value = None
    unit = "mg/dL"

class DurationMeasurement:
    start_datetime = None
    end_datatime = None
    value = None
    unit = "mg/dL/min"