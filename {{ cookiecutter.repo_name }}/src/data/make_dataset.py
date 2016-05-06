# -*- coding: utf-8 -*-
import os
import click
import dotenv
import logging


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    data_dir = os.path.join(os.path.dirname(__file__), '../../data/raw')
    data_path = os.path.join(data_dir, 'dataset.csv.gz')
    # 'touch' file
    with open(data_path, 'a'):
        os.utime(data_path, None)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
    dotenv_path = os.path.join(project_dir, '.env')
    dotenv.load_dotenv(dotenv_path)

    main()
