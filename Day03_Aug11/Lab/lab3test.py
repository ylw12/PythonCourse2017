import unittest
import lab3

class Testlab3Code(unittest.TestCase):

	# Shout
	def test_shout_onlyalpha(self):
		self.assertEqual(lab3.shout("luwei"), "LUWEI!")

	def test_shout_withperiod(self):
		self.assertEqual(lab3.shout("hello."), "HELLO!")

	def test_shout_withesc(self):
		self.assertEqual(lab3.shout("Aha!"), "AHA!")

	def test_shout_error(self):
		self.assertRaises(TypeError, lambda: lab3.reverse(12345))

	# Reverse
	def test_reverse_name(self):
		self.assertEqual(lab3.reverse("Name"), "emaN")

	def test_reverse_nameperiod(self):
		self.assertEqual(lab3.reverse("Name."), ".emaN")

	def test_reverse_exception(self):
		with self.assertRaises(Exception): lab3.reverse("I love you.")

	def test_reverse_error(self):
		self.assertRaises(TypeError, lambda: lab3.reverse(12345))

	# Reverse Words
	def test_reverse_words1(self):
		self.assertEqual(lab3.reversewords("Hello world!"), "world! Hello")

	def test_reverse_words2(self):
		self.assertEqual(lab3.reversewords("I love you"), "you love I")

	def test_reverse_error(self):
		self.assertRaises(TypeError, lambda: lab3.reversewords(12345))

	# Reverse Word Letters
	def test_reverse_a_sentence(self):
		self.assertEqual(lab3.reversewordletters("I love you"), "uoy evol I")

	def test_reverse_another_sentence(self):
		self.assertEqual(lab3.reversewordletters("Hello world!"), "!dlrow olleH")

	def test_reversewordletter_exception(self):
		self.assertRaises(Exception, lambda: lab3.reversewordletters("love"))

	def test_reversewordletter_error(self):
		self.assertRaises(TypeError, lambda: lab3.reversewordletters(12345))

if __name__ == '__main__':
  unittest.main()

