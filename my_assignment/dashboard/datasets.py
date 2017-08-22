from dashboard.models import Nurse, Doctor


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
