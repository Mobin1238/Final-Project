import json

def calculate_transformer_parameters(V1, V2, I1, P=None, A=None, B=1.2, f=50):
    """
    محاسبه پارامترهای ترانسفورماتور EI
    :param V1: ولتاژ اولیه (ولت)
    :param V2: ولتاژ ثانویه (ولت)
    :param I1: جریان اولیه (آمپر)
    :param P: توان (وات)، اختیاری
    :param A: مساحت مقطع هسته (متر مربع)، اختیاری
    :param B: چگالی شار مغناطیسی (تسلا)، پیش‌فرض 1.2
    :param f: فرکانس (هرتز)، پیش‌فرض 50
    :return: دیکشنری شامل مساحت مقطع هسته و تعداد دورهای پیچش اولیه و ثانویه
    """
    results = {}
    
    if A is None and P is not None:
        # محاسبه مساحت مقطع هسته
        A = P / (4.44 * f * B * V1 * I1)
        results['Cross-sectional area (A)'] = A
    
    if A is not None:
        # محاسبه تعداد دورهای پیچش اولیه و ثانویه
        N1 = V1 / (4.44 * f * B * A)
        N2 = V2 / (4.44 * f * B * A)
        results['Primary winding turns (N1)'] = N1
        results['Secondary winding turns (N2)'] = N2
    
    return results

def save_to_file(data, filename='transformer_data.txt'):
    """
    ذخیره داده‌ها در فایل متنی
    :param data: داده‌هایی که باید ذخیره شوند
    :param filename: نام فایل، پیش‌فرض 'transformer_data.txt'
    """
    with open(filename, 'a') as file:
        file.write(json.dumps(data, indent=4))
        file.write('\n')


def example_usage():
    print("ورودی‌های مربوط به محاسبه پارامترهای ترانسفورماتور:")
    V1 = 230.0  # ولتاژ اولیه (ولت)
    V2 = 12.0   # ولتاژ ثانویه (ولت)
    I1 = 0.5    # جریان اولیه (آمپر)
    P = 100.0   # توان (وات)
    A = 0.0001  # مساحت مقطع هسته (متر مربع)

    result = calculate_transformer_parameters(V1, V2, I1, P=P, A=A)
    print("نتایج محاسبات: ", result)

    data_to_save = {
        'Inputs': {
            'V1': V1,
            'V2': V2,
            'I1': I1,
            'P': P,
            'A': A
        },
        'Results': result
    }

    save_to_file(data_to_save)

    print(f"ورودی‌ها و خروجی‌ها در فایل 'transformer_data.txt' ذخیره شدند.")


# اجرای مثال
example_usage()
