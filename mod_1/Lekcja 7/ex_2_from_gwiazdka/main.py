
# Za pomocą from ... import możemy importować zarówno cały moduł jak i pojedyncze funkcje/zmienne

# from school import promotion_status
# from school.grade_calculator import calculate_student_final_grades
# from school.promote import check_promotion
# from school.students_data import is_student_in_school
#
# from school.promote import *
# print(_FAILED_GRADE)
#
# print("Witaj w elektronicznym dzienniku!")
# student_name = input("Podaj imię ucznia żeby dowiedzieć się czy zdał/dała do następnej klasy: ")
#
# if not is_student_in_school(student_name):
#     print(f"Niestety {student_name} nie ma liście...")
# else:
#     final_grades = calculate_student_final_grades(student_name)
#     promotion_result = check_promotion(final_grades)
#
#     if promotion_result == promotion_status.PASSED:
#         print(f"Gratuluje! {student_name} zdał/zdałą do następnej klasy :)")
#     elif promotion_result == promotion_status.FAILED:
#         print(f"Niestety! {student_name} nie zdał/zdałą")
#     else:
#         print("Coś poszło nie tak ")

from school import *
# sam import * patrzy w __init__ pakietu, szuka __all__ lub konkrentych importów

print("Witaj w elektronicznym dzienniku!")
student_name = input("Podaj imię ucznia żeby dowiedzieć się czy zdał/dała do następnej klasy: ")

if not students_data.is_student_in_school(student_name):
    print(f"Niestety {student_name} nie ma liście...")
else:
    final_grades = grade_calculator.calculate_student_final_grades(student_name)
    promotion_result = promote.check_promotion(final_grades)

    if promotion_result == promotion_status.PASSED:
        print(f"Gratuluje! {student_name} zdał/zdałą do następnej klasy :)")
    elif promotion_result == promotion_status.FAILED:
        print(f"Niestety! {student_name} nie zdał/zdałą")
    else:
        print("Coś poszło nie tak ")