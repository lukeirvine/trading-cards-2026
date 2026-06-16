from typing import Optional

from PIL import Image


class ImageBuilder:
    @staticmethod
    def add_image_to_canvas(
        canvas: Image.Image,
        image_path: str,
        size: tuple[int, int],
        position: tuple[int, int],
    ) -> None:
        image = Image.open(image_path)
        image_canvas: Image.Image = ImageBuilder.resize_and_crop_image(image, size)
        canvas.paste(image_canvas, position)

    @staticmethod
    def add_mask_to_canvas(
        canvas: Image.Image,
        mask_path: str,
        size: tuple[int, int],
        position: tuple[int, int],
        fill: Optional[tuple[int, int, int]] = None,
    ) -> None:
        # Open the mask image with an alpha channel
        image = Image.open(mask_path).convert("RGBA")
        # Resize/crop to the desired size
        image = ImageBuilder.resize_and_crop_image(image, size)
        # Use the image’s own alpha channel as the mask
        alpha = image.split()[-1]
        if fill is not None:
            # Create a solid color image with the same size, apply the original alpha
            solid = Image.new("RGBA", image.size, fill + (0,))
            solid.putalpha(alpha)
            canvas.paste(solid, position, alpha)
        else:
            # Paste the original RGBA image onto the canvas, preserving transparency
            canvas.paste(image, position, alpha)

    @staticmethod
    def resize_and_crop_image(image: Image.Image, size: tuple[int, int]) -> Image.Image:
        # Sizes
        current_width, current_height = image.size
        target_width, target_height = size

        # Calculate the aspect ratios
        current_aspect_ratio = current_width / current_height
        new_aspect_ratio = target_width / target_height

        # Calculate the scale factor to resize the image
        if new_aspect_ratio > current_aspect_ratio:
            scale_factor = target_height / current_height
        else:
            scale_factor = target_width / current_width

        # Calculate the new size with the preserved aspect ratio
        resized_width = int(current_width * scale_factor)
        resized_height = int(current_height * scale_factor)

        # Resize the image while maintaining the aspect ratio
        new_size: tuple[int, int] = (resized_width, resized_height)
        resized_image = image.resize(new_size, Image.Resampling.LANCZOS)

        # Calculate the cropping box
        left = (resized_width - target_width) / 2
        top = (resized_height - target_height) / 2
        right = (resized_width + target_width) / 2
        bottom = (resized_height + target_height) / 2

        # Crop the image to the target size
        crop_box = (int(left), int(top), int(right), int(bottom))
        cropped_image = resized_image.crop(crop_box)

        return cropped_image
