from process import process_image
from pathlib import Path
import logging

#job1_path = Path.cwd()
#print(job1_path)

# Run test from the images directory, after activating its venv, with 'python3 -m test.test'
test_path = Path.cwd()
if test_path.name != 'images':
    logging.critical(f'Must run the test module from within the "images" directory. Current directory: {test_path}')
    exit(-1)

process_image.run_job(test_path / 'test' / 'job1', lambda i: process_image.image_invert_color(i))

process_image.run_job(test_path / 'test' / 'job2', lambda i: process_image.image_resize(i, (300, 300)))