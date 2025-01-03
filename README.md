# CurrencyExchangeBot

CurrencyExchangeBot — это Telegram-бот, позволяющий взаимодействовать с валютами и обменниками через удобные команды.

## Установка и запуск

### Требования

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

### Как использовать прилолжение

1. **Склонируйте приложение**

   ```bash
   git clone https://github.com/namig41/CurrencyExchangeBot.git
   cd CurrencyExchangeBot
   ```

2. Установите все необходимые пакеты из раздела требования

### Реализованные команды

* `make app-start` - запуск приложения и базы данных/инфраструктуры
* `make app-logs` - отслеживание журналов в контейнере приложения
* `make app-drop` - остановка приложения и всей инфраструктуры
* `make shell` - переход в интерактивную оболочку bash

## Команды

- **`/start`** — Приветствие.
- **`/currency <код валюты>`** — Узнать информацию о валюте.
- **`/currency_add <Название валюты> | <Код валюты> | <Символ>`** — Добавить новую валюту.
- **`/currencies`** — Список всех валют.
- **`/exchange_rate <код базовой валюты> <код целевой валюты>`** — Узнать информацию об обменнике.
- **`/exchange_rate_add <Базовая валюта> | <Целевая валюта> | <Курс>`** — Добавить новый обменник.
- **`/exchange_rates`** — Список всех обменников.
- **`/exchange <Базовая валюта> | <Целевая валюта> | <Средства>`** — Перевод с одной валюты в другую.

## Пример команды

Чтобы узнать курс обмена, введите:
```
/exchange_rate USD EUR
```

Для добавления новой валюты:
```
/currency_add Доллар | USD | $
```