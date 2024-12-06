import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    substring = ""
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        # not sure we get the closing delimiter with here... <-- this must be checked
        if node.text.count(delimiter) > 0:
            if node.text.count(delimiter) != 2: 
                raise Exception("closing delimiter not found")
            substring = node.text.split(delimiter)[1].split(delimiter)[0]

        
        split = node.text.split(delimiter)

        for string in split:
            if string == substring:
                new_nodes.append(TextNode(substring, text_type))
            else:
                new_nodes.append(TextNode(string, TextType.TEXT))
            
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) 
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text) 
     