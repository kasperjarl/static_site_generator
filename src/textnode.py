from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image" 

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_TextNode):
        # checks if two TextNodes are identical
        return (
            self.text == other_TextNode.text
            and self.text_type == other_TextNode.text_type
            and self.url == other_TextNode.url
        )
    
    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")
    
