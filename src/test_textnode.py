import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC, "")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2) 


if __name__ == "__main__":
    unittest.main()