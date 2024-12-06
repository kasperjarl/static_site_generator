import unittest
from standalone_funcs import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct = [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word", TextType.TEXT),
                ]
        
        self.assertEqual(new_nodes, correct)

    def test_eq2(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct = [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("bolded phrase", TextType.BOLD),
                    TextNode(" in the middle", TextType.TEXT),
                ]
        
        self.assertEqual(new_nodes, correct)

    def test_not_eq1(self):
        node = TextNode("This is text with a **bol1ded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct = [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("bolded phrase", TextType.BOLD),
                    TextNode(" in the middle", TextType.TEXT),
                ]
        
        self.assertNotEqual(new_nodes, correct)

    def test_missing_end_delimiter(self):
        node = TextNode("This is text with a **bolded phrase in the middle", TextType.TEXT)
        
        with self.assertRaises(Exception) as context:
            node.new_nodes = split_nodes_delimiter([node], "**", TextType.CODE)
        
        self.assertEqual(str(context.exception), "closing delimiter not found")

    def test_all_text(self):
        node = TextNode("This is all normal text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct = [
                    TextNode("This is all normal text", TextType.TEXT),
                ]
        
        self.assertEqual(new_nodes, correct)

    def test_extract_markdown_images_eq(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        res = extract_markdown_images(text)
        correct = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        
        self.assertEqual(res, correct)

    def test_extract_markdown_images_not_eq(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        res = extract_markdown_images(text)
        correct = [('ricks roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        
        self.assertNotEqual(res, correct)

    def test_extract_markdown_links_eq(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        res = extract_markdown_links(text)
        correct = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        
        self.assertEqual(res, correct)

    def test_extract_markdown_links_not_eq(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        res = extract_markdown_links(text)
        correct = [("to boot d2ev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        
        self.assertNotEqual(res, correct)