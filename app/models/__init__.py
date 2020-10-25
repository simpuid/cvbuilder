from .user import User, populate_users
from .student import Student
from .tenth import Tenth
from .twelfth import Twelfth
from .skill import Skill
from .professor import Professor, populate_professors
from .achievement import Achievement

__all__ = ["User", "populate_users", "Student", "Tenth", "Twelfth", "Skill", "Professor", "populate_professors",
           "Achievement"]
