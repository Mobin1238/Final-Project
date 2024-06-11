def perform_convolution(input_list, filter_list):
    size_input = len(input_list)
    size_filter = len(filter_list)
    output_list = [0] * (size_input + size_filter - 1)

    for output_index in range(size_input + size_filter - 1):
        for filter_index in range(max(0, output_index - size_filter + 1), min(size_input, output_index + 1)):
            output_list[output_index] += input_list[filter_index] * filter_list[output_index - filter_index]

    return output_list

input_data = [1, 2, 3, 4]
filter_data = [0.5, 0.25, 0.1]

result = perform_convolution(input_data, filter_data)

output_path = 'C:\\Users\\Rayan system\\Desktop\\Mobin_Final\\Mobin_Final\\convolution_output.txt'

with open(output_path, 'w') as file:
    file.write(f"Input Data: {input_data}\n")
    file.write(f"Filter Data: {filter_data}\n")
    file.write(f"Output Data: {result}\n")

print(f"ورودی‌ها و خروجی‌ها در مسیر '{output_path}' ذخیره شدند.")
