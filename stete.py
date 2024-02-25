from aiogram.dispatcher.filters.state import StatesGroup, State

class SignUpState(StatesGroup):
    full_name = State()
    age = State()
    status = State()
    phone = State()
    confirm = State()