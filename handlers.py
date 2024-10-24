import json
from aiogram import Bot, types
from aiogram.filters import Command
from aiogram import Router
from utils import add_matrices, subtract_matrices, multiply_matrices, determinant
from profile import add_matrix_to_profile, add_operation_to_profile, get_user_profile

router = Router()


def register_handlers(dp, bot: Bot):
    dp.include_router(router)


def parse_matrix(matrix_str):
    try:
        matrix = json.loads(matrix_str)
        if isinstance(matrix, list):
            return matrix
        return None
    except json.JSONDecodeError:
        return None


@router.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer("Пожалуйста, отправьте матрицу в формате JSON.")


@router.message(Command('add_matrix'))
async def add_matrix_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите матрицу после команды.")
        return
    matrix = parse_matrix(args[1])
    if matrix is None:
        await message.answer("Используйте JSON.")
        return
    add_matrix_to_profile(user_id, matrix)
    await message.answer(f"Матрица сохранена: {matrix}")


@router.message(Command('add_matrices'))
async def add_matrices_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.answer("Пожалуйста, укажите две матрицы после команды.")
        return
    matrix1 = parse_matrix(args[1])
    matrix2 = parse_matrix(args[2])
    if matrix1 is None or matrix2 is None:
        await message.answer("Используйте JSON.")
        return
    result = add_matrices(matrix1, matrix2)
    add_operation_to_profile(user_id, 'Сложение', matrix2, result)
    await message.answer(f"Результат сложения: {result}")


@router.message(Command('subtract_matrices'))
async def subtract_matrices_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.answer("Пожалуйста, укажите две матрицы после команды.")
        return
    matrix1 = parse_matrix(args[1])
    matrix2 = parse_matrix(args[2])
    if matrix1 is None or matrix2 is None:
        await message.answer("Используйте JSON.")
        return
    result = subtract_matrices(matrix1, matrix2)
    add_operation_to_profile(user_id, 'Вычитание', matrix2, result)
    await message.answer(f"Результат вычитания: {result}")


@router.message(Command('multiply_matrices'))
async def multiply_matrices_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.answer("Пожалуйста, укажите две матрицы после команды.")
        return
    matrix1 = parse_matrix(args[1])
    matrix2 = parse_matrix(args[2])
    if matrix1 is None or matrix2 is None:
        await message.answer("Используйте JSON.")
        return
    result = multiply_matrices(matrix1, matrix2)
    add_operation_to_profile(user_id, 'Умножение', matrix2, result)
    await message.answer(f"Результат умножения: {result}")


@router.message(Command('determinant'))
async def determinant_command(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите матрицу после команды.")
        return
    matrix = parse_matrix(args[1])
    if matrix is None:
        await message.answer("Используйте JSON.")
        return
    result = determinant(matrix)
    add_operation_to_profile(user_id, 'Определитель', None, result)
    await message.answer(f"Определитель матрицы: {result}")


@router.message(Command('profile'))
async def profile_command(message: types.Message):
    user_id = message.from_user.id
    profile = get_user_profile(user_id)
    if profile:
        await message.answer(profile)
    else:
        await message.answer("Ваш профиль пока пуст.")
