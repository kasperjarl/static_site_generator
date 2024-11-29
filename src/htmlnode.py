class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return None
        
        if not isinstance(self.props, dict):
            raise TypeError("props must be a dictionary")
        
        string = " "
        i = 0
        for key in self.props:
            string += f'{key}="{self.props[key]}"'
            if i+1 <= len(self.props):
                string += " "
        
        return string  
    
    def __eq__(self, value):
        return(
            self.tag == value.tag
            and self.value == value.value
            and self.children == value.children
            and self.props == value.props
        )

    def __repr__(self):
        return (
            f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
            )


class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=None)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        elif not self.tag:
            return f"{self.value}"
        elif self.props:
            return f'<{self.tag} href="{self.props["href"]}">{self.value}</{self.tag}>'
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
