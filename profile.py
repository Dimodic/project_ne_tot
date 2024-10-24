import sqlite3
import json
from database import get_db_connection


def add_matrix_to_profile(user_id, matrix):
    conn = get_db_connection()
    cursor = conn.cursor()

    matrix_str = json.dumps(matrix)

    cursor.execute('INSERT INTO profiles (user_id, matrix) VALUES (?, ?)', (user_id, matrix_str))
    conn.commit()
    conn.close()


def add_operation_to_profile(user_id, operation_type, matrix2, result):
    conn = get_db_connection()
    cursor = conn.cursor()

    matrix1_str = cursor.execute('SELECT matrix FROM profiles WHERE user_id = ? ORDER BY id DESC LIMIT 1', (user_id,)).fetchone()[0]
    matrix2_str = json.dumps(matrix2) if matrix2 else None
    result_str = json.dumps(result)

    cursor.execute('INSERT INTO operations (user_id, operation_type, matrix1, matrix2, result) VALUES (?, ?, ?, ?, ?)',
                   (user_id, operation_type, matrix1_str, matrix2_str, result_str))
    conn.commit()
    conn.close()


def get_user_profile(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT matrix FROM profiles WHERE user_id = ?', (user_id,))
    matrices = cursor.fetchall()

    cursor.execute('SELECT operation_type, matrix1, matrix2, result FROM operations WHERE user_id = ?', (user_id,))
    operations = cursor.fetchall()

    conn.close()

    if matrices:
        profile = "Ваш профиль:\n\nВведенные матрицы:\n"
        for matrix in matrices:
            matrix_data = json.loads(matrix[0])
            profile += f"{matrix_data}\n"
        profile += "\nОперации:\n"
        for op in operations:
            matrix1_data = json.loads(op[1])
            matrix2_data = json.loads(op[2]) if op[2] else "N/A"
            result_data = json.loads(op[3])
            profile += f"{op[0]}:\nМатрица 1: {matrix1_data}\nМатрица 2: {matrix2_data}\nРезультат: {result_data}\n\n"
        return profile
    return None
