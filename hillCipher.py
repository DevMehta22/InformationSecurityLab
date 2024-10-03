def conversion(): 
    letter_to_num, num_to_letter = {}, {}
    for idx in range(26):
        letter = chr(idx + 65)
        letter_to_num[letter] = idx
        num_to_letter[idx] = letter
    return letter_to_num, num_to_letter

def find_inverse_2x2(matrix):
    determinant = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    if determinant == 0:
        return None
    for num in range(26):
        if (determinant * num) % 26 == 1:
            modular_inverse = num
            break
    else:
        return None
    return [
        [(matrix[1][1] * modular_inverse) % 26, (-matrix[0][1] * modular_inverse) % 26],
        [(-matrix[1][0] * modular_inverse) % 26, (matrix[0][0] * modular_inverse) % 26]
    ]

def matrix_vector_mult(matrix, vec):
    result = [0, 0]
    for row_idx in range(2):
        for col_idx in range(2):
            result[row_idx] += matrix[row_idx][col_idx] * vec[col_idx]
            result[row_idx] %= 26
    return result

def convert_key_matrix_to_nums(matrix, mapping):
    return [[mapping[char] for char in row] for row in matrix]

def encrypt(plain_text, key_matrix):
    letter_to_num, num_to_letter = conversion()
    numeric_key = convert_key_matrix_to_nums(key_matrix, letter_to_num)
    plain_text = ''.join([char for char in plain_text.upper() if char.isalpha()])
    if len(plain_text) % 2 != 0:
        plain_text += 'X'
    encrypted_text = ""
    for idx in range(0, len(plain_text), 2):
        pair = plain_text[idx:idx+2]
        vec = [letter_to_num[pair[0]], letter_to_num[pair[1]]]
        encrypted_vec = matrix_vector_mult(numeric_key, vec)
        encrypted_text += num_to_letter[encrypted_vec[0]] + num_to_letter[encrypted_vec[1]]
    return encrypted_text

def decrypt(cipher_text, key_matrix):
    letter_to_num, num_to_letter = conversion()
    numeric_key = convert_key_matrix_to_nums(key_matrix, letter_to_num)
    inv_key_matrix = find_inverse_2x2(numeric_key)
    if inv_key_matrix is None:
        return "Key matrix is not invertible."
    decrypted_text = ""
    for idx in range(0, len(cipher_text), 2):
        pair = cipher_text[idx:idx+2]
        vec = [letter_to_num[pair[0]], letter_to_num[pair[1]]]
        decrypted_vec = matrix_vector_mult(inv_key_matrix, vec)
        decrypted_text += num_to_letter[decrypted_vec[0]] + num_to_letter[decrypted_vec[1]]
    return decrypted_text

key_grid = [['D', 'D'], ['C', 'F']]
plain_message = "EXAMOVER"

cipher_output = encrypt(plain_message, key_grid)
print(f"Ciphertext: {cipher_output}")

decrypted_output = decrypt(cipher_output, key_grid)
print(f"Decrypted Text: {decrypted_output}")
