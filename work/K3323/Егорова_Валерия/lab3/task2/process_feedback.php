<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' || $_SERVER['REQUEST_METHOD'] == 'GET') {
    // Определяем источник данных (POST или GET)
    $input = $_SERVER['REQUEST_METHOD'] == 'POST' ? $_POST : $_GET;

    // Получаем значения из формы
    $first_name = htmlspecialchars($input['first_name'] ?? 'Не указано');
    $surname = htmlspecialchars($input['surname'] ?? 'Не указано');
    $email = htmlspecialchars($input['email'] ?? 'Не указано');
    $feedback = htmlspecialchars($input['feedback'] ?? 'Не указано');
    $gender = $input['gender'] ?? 'Не указан';

    // Обрабатываем значения чекбоксов
    $sources = isset($input['source']) && is_array($input['source']) ? implode(', ', $input['source']) : 'Не указано';

    // Выводим полученные данные
    echo "<h1>Спасибо за отзыв</h1>";
    echo "<p><strong>Имя:</strong> $first_name</p>";
    echo "<p><strong>Фамилия:</strong> $surname</p>";
    echo "<p><strong>Электронная почта:</strong> $email</p>";
    echo "<p><strong>Обратная связь:</strong> $feedback</p>";
    echo "<p><strong>Пол:</strong> $gender</p>";
    echo "<p><strong>Откуда узнали о сайте:</strong> $sources</p>";
} else {
    echo "<p>Ошибка: форма не была отправлена корректно.</p>";
}
?>
