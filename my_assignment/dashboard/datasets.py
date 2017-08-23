from dashboard.models import Nurse, Doctor, Department, Patient


def doctors_unavailable_available():
    num_of_available_doctors = len(Doctor.objects.filter(occupied=False))
    num_of_unavailable_doctors = len(Doctor.objects.filter(occupied=True))

    return [num_of_available_doctors,
            num_of_unavailable_doctors]


def nurses_unavailable_available():
    num_of_available_nurses = len(Nurse.objects.filter(occupied=False))
    num_of_unavailable_nurses = len(Nurse.objects.filter(occupied=True))

    return [num_of_available_nurses,
            num_of_unavailable_nurses]

def department_patients():
    in_neuro = len(Patient.objects.filter(department='Neuro'))
    in_cardio = len(Patient.objects.filter(department='Cardio'))
    in_trauma = len(Patient.objects.filter(department='Trauma'))
    in_ent = len(Patient.objects.filter(department='ENT'))
    in_gs = len(Patient.objects.filter(department='General Surgery'))
    in_maternity = len(Patient.objects.filter(department='Maternity'))
    in_oncology = len(Patient.objects.filter(department='Oncology'))
    in_urology = len(Patient.objects.filter(department='Urology'))

    return [in_neuro, in_cardio, in_trauma, in_ent, in_gs, in_maternity, in_oncology, in_urology]
