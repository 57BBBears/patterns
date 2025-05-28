from implementation.image import Image
from implementation.proxy import ImageProxy

if __name__ == "__main__":
    image_url = "https://test.com?image=test.jpg"

    image = Image(image_url)
    assert image.image == b"test.jpg"
    print("Real image")
    print(image.image)
    print(image.extent)

    image_proxy = ImageProxy(image_url)
    assert image_proxy.extent != image.extent
    print("Proxy image")
    print("Fake", image_proxy.extent)
    assert image_proxy.image == image.image
    assert image_proxy.extent == image.extent
    print("Original", image_proxy.extent)
