from chat.factories import ChatFactory
from classes.factories import CategoryFactory, MentoringFactory, ReviewFactory
from schedules.factories import ScheduleFactory
from users.factories import MentorFactory, StudentFactory

def populate_database():
    categories = CategoryFactory.create_batch(5)
    print(f'Created {len(categories)} categories')

    mentors = MentorFactory.create_batch(10)
    print(f'Created {len(mentors)} mentors')

    students = StudentFactory.create_batch(20)
    print(f'Created {len(students)} students')

    mentorings = MentoringFactory.create_batch(10)
    print(f'Created {len(mentorings)} mentorings')

    reviews = ReviewFactory.create_batch(15)
    print(f'Created {len(reviews)} reviews')

    schedules = ScheduleFactory.create_batch(12)
    print(f'Created {len(schedules)} schedules')

    messages = ChatFactory.create_batch(20)
    print(f'Created {len(messages)} messages')

    print("DB Successfully populated")
