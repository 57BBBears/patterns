from helpers.image import ImageDownloader
from implementation.builders import HTMLBuilder, ImageBuilder
from implementation.director import DocumentDirector

if __name__ == "__main__":
    director = DocumentDirector("test title", "test content")
    html_builder = HTMLBuilder()
    image_builder = ImageBuilder(ImageDownloader())

    # Make html version
    director.make_excerpt(html_builder)
    print(html_builder.get_result())
    director.make_document(html_builder)
    print(html_builder.get_result())

    # Make image version
    director.make_excerpt(image_builder)
    print(image_builder.get_result())
    director.make_document(image_builder)
    print(image_builder.get_result())
