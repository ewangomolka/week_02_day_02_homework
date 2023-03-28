import unittest
from src.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.john = Person("John Mclain", 0)
        self.holly = Person("Holly Gennero", 0)
        self.badguy1 = Person("Hans Gruber", 0)

    
    def test_mclain_starts_with_no_kills(self):
        self.assertEqual(0, self.john.no_of_kills)

    
    def test_add_kill(self):
        self.john.add_kill()
        self.assertEqual(1, self.john.no_of_kills)
        
    # Extension
    # Write a test to check if Holly is using her maiden name again.
    def test_is_holly_using_her_maiden_name_again(self):
        self.assertEqual("Holly is using her maiden name again", self.holly.check_name())
    # Extension
    # Write a check to check Hans Gruber hasn't killed anyone yet.
    def test_has_hans_gruber_killed_anyone_yet(self):
        self.assertEqual(0, self.badguy1.no_of_kills)
    
