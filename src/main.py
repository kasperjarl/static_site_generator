from textnode import TextNode, TextType

def main():
    test_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    
    print(repr(test_node))


if __name__ == "__main__":
    main()
