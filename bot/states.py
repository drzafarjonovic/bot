from aiogram.fsm.state import StatesGroup, State

class TriageStates(StatesGroup):
    waiting_for_symptoms = State()
