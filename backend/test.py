def test_func(text, file_name):
    with open(f'{file_name}.txt', "w") as file:
        file.write(text)   