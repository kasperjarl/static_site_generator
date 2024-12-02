import unittest

from htmlnode import HTMLNODE, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
        
        def test_empty_tag(self):
            node = ParentNode(
                "",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            with self.assertRaises(ValueError) as context:
                node.to_html()     

        def test_empty_children(self):
            node = ParentNode(
                "p",
                [],
            )
            with self.assertRaises(ValueError) as context:
                node.to_html()   
              
        def test_eq(self):
            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            test = node.to_html()
            equals = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
            self.assertEquals(test, equals)       

        def test_nested_parentnodes(self):
            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ParentNode("x",
                       [LeafNode("c", "code text"),
                        ParentNode("d",[LeafNode("i", "you killed kenny"),],)
                        ],)
                ],
            )    
            test = node.to_html()
            equals = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<x><c>code text</c><d><i>you killed kenny</i></d></x></p>"
            self.assertEquals(test, equals)   

        def test_missing_value_in_childrens_leafnodes(self):
            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, None),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            with self.assertRaises(ValueError) as context:
                node.to_html()   