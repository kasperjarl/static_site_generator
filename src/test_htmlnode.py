import unittest
from htmlnode import HTMLNODE, LeafNode
from textnode import TextType, TextNode

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

    def test_text_node_to_html_node_TEXT(self):
        text_node = TextNode("this should just be normal text", TextType.TEXT)
        node = HTMLNODE.text_node_to_html_node(text_node).to_html()
        correct = "this should just be normal text"
        self.assertEqual(node, correct)

    def test_text_node_to_html_node_Bold(self):
        text_node = TextNode("this should just be normal text", TextType.BOLD)
        node = HTMLNODE.text_node_to_html_node(text_node).to_html()
        correct = "<b>this should just be normal text</b>"
        self.assertEqual(node, correct)

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("this should just be normal text", TextType.ITALIC)
        node = HTMLNODE.text_node_to_html_node(text_node).to_html()
        correct = "<i>this should just be normal text</i>"
        self.assertEqual(node, correct)

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("this should just be normal text", TextType.CODE)
        node = HTMLNODE.text_node_to_html_node(text_node).to_html()
        correct = "<code>this should just be normal text</code>"
        self.assertEqual(node, correct)

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Click me", TextType.LINK, "https://boot.dev")
        node = HTMLNODE.text_node_to_html_node(text_node).to_html()
        correct = '<a href="https://boot.dev">Click me</a>'
        self.assertEqual(node, correct)

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Alt text description", TextType.IMAGE, "https://example.com/image.png")
        node = HTMLNODE.text_node_to_html_node(text_node).to_html()
        correct = '<img src="https://example.com/image.png" alt="Alt text description" />'
        self.assertEqual(node, correct)