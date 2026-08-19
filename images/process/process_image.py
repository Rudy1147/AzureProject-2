import cv2
import re
import logging
from collections import namedtuple
from pathlib import Path

Size = namedtuple('Size', ['x', 'y'])

# TODO: Implement reading an image from the storage account, which will require
# some authorization, probably an Entra ID RBAC for whomever runs this script.

# TEMP: For now, we assume the file to process is local and can be opened with
# the passed path.
def open_image_path(path: str):
    # NOTE: This function can except, and should be caught within a try block.

    # Use regular expressions to parse out the file type for reading.
    expression = re.match(r'(.+)\.(.*)', path.strip())

    if not expression.group(0):
        logging.error(f'Invalid file path: {path}')
        raise FileNotFoundError()
    if not expression.group(1):
        logging.warning(f'No file extension passed: {path}')

    return cv2.imread(path)

# Expects a path to a directory with an input and output folder.
def run_job(job_path: str, image_function: function):
    job_dir = Path(job_path)
    if not job_dir.is_dir():
        raise FileNotFoundError(f'Invalid job path: {job_path}')
    
    input_dir = job_dir / 'input'
    if not input_dir.is_dir():
        raise FileNotFoundError(f'No job "input" directory within path: {job_path}')

    output_dir = job_dir / 'output'
    output_dir.mkdir(exist_ok=True)

    for item in input_dir.iterdir():
        if item.is_file():
            # TODO: Probably use a try block to catch failed files, and keep
            # processing other files.
            abs_path = item.resolve()
            logging.info(f'Processing {abs_path}')

            input_image = cv2.imread(abs_path)
            output_image = image_function(input_image)
            output_path = (output_dir / item.name).resolve()
            cv2.imwrite(output_path, output_image)

    logging.info(f'Finished processing {job_dir.name}')
    return True

# Calls the resize function on an imported image.
def image_resize(image, new_size: Size):
    # See: https://www.geeksforgeeks.org/python/image-resizing-using-opencv-python/
    return cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)

# Inverts color on an imported image.
def image_invert_color(image):
    # Flips all bits in the image, giving us the inverse color.
    # See: https://www.geeksforgeeks.org/python/arithmetic-operations-on-images-using-opencv/
    return cv2.bitwise_not(image)
