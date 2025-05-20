from interfaces.builder import DocumentBuilder


class DocumentDirector:
    """Orchestrates the creation of different types of documents."""

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def make_document(self, builder: DocumentBuilder):
        builder.reset()
        builder.build_header(self.title)
        builder.build_title(self.title)
        builder.build_content(self.content)
        builder.build_footer()

    def make_excerpt(self, builder: DocumentBuilder):
        builder.reset()
        builder.build_title(self.title)
        builder.build_content(self.content)
