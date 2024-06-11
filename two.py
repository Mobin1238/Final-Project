import numpy as np
import json

def calculate_electric_field(grid):
    k = 8.99e9  # ثابت کولن در N·m²/C²
    
    # پیدا کردن نقطه O
    O_position = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                O_position = (i, j)
                break
        if O_position:
            break
            
    if not O_position:
        raise ValueError("Grid must contain a single 'O' point.")
    
    Ex, Ey = 0, 0
    Ox, Oy = O_position
    
    # محاسبه میدان الکتریکی ناشی از بارها در نقطه O
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0 and grid[i][j] != 'O':
                q = grid[i][j]
                dx, dy = j - Oy, i - Ox
                r = np.sqrt(dx**2 + dy**2)
                if r == 0:
                    continue
                E = k * q / r**2
                Ex += E * (dx / r)
                Ey += E * (dy / r)
    
    return [Ex, Ey]

def electric_field_line_charge(lambda_l, d):
    k = 8.99e9  # ثابت کولن در N·m²/C²
    E = 2 * k * lambda_l / d
    return E

def save_to_file(data, filename='electric_field_data.txt'):
    """
    ذخیره داده‌ها در فایل متنی
    :param data: داده‌هایی که باید ذخیره شوند
    :param filename: نام فایل، پیش‌فرض 'electric_field_data.txt'
    """
    with open(filename, 'a') as file:
        file.write(json.dumps(data, indent=4))
        file.write('\n')


def example_usage():
    print("ورودی‌های مربوط به محاسبه میدان الکتریکی در نقطه O:")
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 'O', 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    result_point_charge = calculate_electric_field(grid)
    print("میدان الکتریکی در نقطه O: ", result_point_charge)

    print("\nورودی‌های مربوط به محاسبه میدان الکتریکی ناشی از خط باردار:")
    lambda_l = 1e-6  # چگالی بار خطی (C/m)
    d = 1  # فاصله (متر)

    # محاسبه میدان الکتریکی ناشی از خط باردار
    E_line = electric_field_line_charge(lambda_l, d)
    print("میدان الکتریکی در فاصله یک متری از خط باردار: ", E_line)

    data_to_save = {
        'Inputs_Point_Charge': {
            'grid': grid
        },
        'Results_Point_Charge': result_point_charge,
        'Inputs_Line_Charge': {
            'lambda_l': lambda_l,
            'd': d
        },
        'Results_Line_Charge': E_line
    }

    save_to_file(data_to_save)

    print(f"ورودی‌ها و خروجی‌ها در فایل 'electric_field_data.txt' ذخیره شدند.")


# اجرای مثال
example_usage()
