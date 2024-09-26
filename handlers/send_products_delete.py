import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM products p
    INNER JOIN products_detail pd ON p.product_id = pd.product_id
    """).fetchall()
    conn.close()
    return products

def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("""DELETE FROM products WHERE product_id = ?""", (product_id,))
    conn.commit()
    conn.close()


async def start_send(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Все товары', callback_data='show_all_delete')
    keyboard.add(button)

async def send_all_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()
    if products:
        for product in products:
            caption = (f"Артикул - {product['product_id']}\n"
                       f"Название товара - {product['name_product']}\n"
                       f"Информация о товаре - {product['info_product']}\n"
                       f"категория - {product['category']}\n"
                       f"Размер - {product['size']}\n"
                       f"Цена - {product['price']} сом\n")

            delete_product_markup = InlineKeyboardMarkup(resize_keyboard=True)
            delete_product_button = InlineKeyboardButton('Удалить',
                                                         callback_data=f'delete_{product["product_id"]}')
            delete_product_markup.add(delete_product_button)

            await callback_query.message.answer_photo(photo=product['photo'],
                                                      caption=caption,
                                                      reply_markup=delete_product_markup)
    else:
        await callback_query.message.answer("Товары не найдены!")



async def delete_product_callback(callback_query: types):
    product_id = int(callback_query.data.split('_')[1])

    delete_product(product_id)

    await callback_query.answer('Товар удален!')


def register_send_delete_product(dp: Dispatcher):
    dp.register_message_handler(start_send, commands=['send_products_delete'])
    dp.register_callback_query_handler(send_all_products,
                                       Text(equals='show_all_delete'))
    dp.register_callback_query_handler(delete_product_callback, Text(startswith='delete_'))




