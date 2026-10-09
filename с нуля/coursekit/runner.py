"""Запуск программ студентов для автопроверки.

Используется тестами: программа студента выполняется как отдельный процесс,
ей подаётся стандартный ввод и возвращается стандартный вывод.
"""
from __future__ import annotations

import os
import subprocess
import sys

TIMEOUT_SECONDS = 10


def run_script(script_path, stdin_text: str = "") -> str:
    """Запустить программу студента и вернуть её стандартный вывод.

    script_path -- путь к .py-файлу задачи;
    stdin_text  -- строки ввода, «набираемые» пользователем.

    Если программа завершилась ошибкой, зависла или не найдена —
    возбуждается AssertionError с человекочитаемым объяснением.
    """
    script = str(script_path)
    if not os.path.exists(script):
        raise AssertionError(
            f"Не найден файл задачи: {script}.\n"
            "Проверьте, что вы запускаете тест из копии курса с сохранённой структурой папок."
        )

    # UTF-8 принудительно: иначе на Windows вывод в конвейере кодируется
    # в кодовую страницу консоли (cp1251/cp866) и русский текст «ломается».
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    try:
        proc = subprocess.run(
            [sys.executable, script],
            input=stdin_text,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=TIMEOUT_SECONDS,
            env=env,
        )
    except subprocess.TimeoutExpired:
        raise AssertionError(
            f"Программа работала дольше {TIMEOUT_SECONDS} секунд.\n"
            "Похоже, она ждёт ввода, которого не происходит: посчитайте количество "
            "вызовов input() — строк ввода в тесте ровно столько, сколько указано в условии."
        ) from None

    if proc.returncode != 0:
        raise AssertionError(
            "Программа завершилась с ошибкой ( traceback ниже ):\n"
            + (proc.stderr.strip() or "(сообщения нет)")
        )
    return proc.stdout


def out_lines(stdout: str) -> list[str]:
    """Разбить вывод программы на строки, убрав концевые пробелы."""
    return [line.rstrip() for line in stdout.strip("\n").splitlines()]
