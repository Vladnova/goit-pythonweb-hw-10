from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import pool
from alembic import context
import asyncio
from src.database.models import Base
from src.conf.config import config as app_config

# Об'єкт конфігурації Alembic
config = context.config

# Налаштування логування
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Встановлюємо метадані моделі для автогенерації міграцій
target_metadata = Base.metadata

# Встановлюємо URL бази даних із конфігурації
config.set_main_option("sqlalchemy.url", app_config.DB_URL)


def run_migrations_offline() -> None:
    """Виконання міграцій в офлайн-режимі."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations(connection):
    """Виконання міграцій із підключенням."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    """Асинхронне виконання міграцій."""
    # Створюємо асинхронний двигун
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),  # Отримуємо URL із конфігурації
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Виконання міграцій в онлайн-режимі."""
    asyncio.run(run_async_migrations())


# Визначаємо режим і запускаємо відповідну функцію
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
