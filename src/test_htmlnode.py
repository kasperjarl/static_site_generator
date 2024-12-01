import unittest
from htmlnode import HTMLNODE, LeafNode

class TestHtmlNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNODE()
        node2 = HTMLNODE()
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = HTMLNODE("hey", "you", "could", "be")
        node2 = HTMLNODE("hey", "you", "could", "be")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNODE("hey", "you", "could", "None")
        node2 = HTMLNODE("hey", "you", "could")
        self.assertNotEqual(node, node2)
    
    def test_props_to_html(self):
        node = HTMLNODE("hey", "you", "could", {
                                                "href": "https://www.google.com", 
                                                "target": "_blank",
                                            })
        node2 = HTMLNODE("hey", "you", "could", {
                                                "href": "https://www.google.com", 
                                                "target": "_blank",
                                            })
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_props_to_html2(self):
        node = HTMLNODE("hey", "you", "could", {
                                                "href": "https://www.google.com", 
                                                "target": "_blank",
                                            })
        node2 = HTMLNODE("hey", "you", "could", {
                                                "href": "https://www.google.com", 
                                                "target": "_blnk",
                                            })
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_props_to_html_raises_exception(self):
        node = HTMLNODE("a", "b", "c", "d")  # Incorrect type for props
        with self.assertRaises(TypeError) as context:
            node.props_to_html()
        
        self.assertEqual(str(context.exception), "props must be a dictionary")

    def test_LeafNode_eq(self):
        leaf_test = LeafNode("p", "This is a paragraph of text.")
        leaf_test1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_test, leaf_test1)

    def test_LeafNode_eq(self):
        leaf_test = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leaf_test1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_test, leaf_test1)

    def test_LeafNode_eq(self):
        leaf_test = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        leaf_test1 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(leaf_test, leaf_test1)