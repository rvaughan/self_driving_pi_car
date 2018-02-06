import argparse
from Config import Config
from DataHolder import DataHolder


def records_generator(channels,
                      data_path,
                      label_path,
                      name,
                      flip=False,
                      augmentation=False,
                      gray=False,
                      green=False,
                      binary=False):
    """
    Generates tfrecords.

    :param config: config class with all hyper param information
    :type config: Config
    :param data_path: path to load data np.array
    :type data_path: str
    :param record_path: path to load labels np.array
    :type label_path: str
    :param name: path to save tfrecord
    :type name: str
    :param flip: param to control if the data
                         will be flipped
    :type flip: boolean
    :param augmentation: param to control if the data
                         will augmented
    :type augmentation: boolean
    :param gray: param to control if the data
                 will be grayscale images
    :type gray: boolean
    :param green: param to control if the data will use only
                  the green channel
    :type green: boolean
    :param binary: param to control if the data will be binarized
    :type binary: boolean
    """

    config = Config(channels=channels)
    data = DataHolder(config,
                      data_path=data_path,
                      label_path=label_path,
                      record_path=name,
                      flip=flip,
                      augmentation=augmentation,
                      gray=gray,
                      green=green,
                      binary=binary,
                      records=None)
    data.create_records()


def main():
    """
    Main script to perform data search.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n",
                        "--name",
                        type=str,
                        default="data",
                        help="name for tfrecords e.g. pure, flip, aug, bin, gray, green (default=data)")  # noqa

    parser.add_argument("-f",
                        "--flip",
                        action="store_true",
                        default=False,
                        help="flag to flip x-axis (default=False)")

    parser.add_argument("-p",
                        "--pure",
                        action="store_true",
                        default=False,
                        help="flag to pure (default=False)")

    parser.add_argument("-a",
                        "--augmentation",
                        action="store_true",
                        default=False,
                        help="flag to augment dataset (default=False)")

    parser.add_argument("-gy",
                        "--gray",
                        action="store_true",
                        default=False,
                        help="flag to transform dataset in grayscale (default=False)")  # noqa

    parser.add_argument("-gr",
                        "--green",
                        action="store_true",
                        default=False,
                        help="flag to keep only the green channel (default=False)")  # noqa

    parser.add_argument("-b",
                        "--binary",
                        action="store_true",
                        default=False,
                        help="flag to binarize dataset (default=False)")

    parser.add_argument("-d",
                        "--train_data",
                        type=str,
                        default=None,
                        help="train data path (default=None)")

    parser.add_argument("-l",
                        "--train_label",
                        type=str,
                        default=None,
                        help="label data path (default=None)")

    args = parser.parse_args()
    if args.binary or args.green or args.gray:
        channels = 1
    else:
        channels = 3
    records_generator(channels,
                      args.train_data,
                      args.train_label,
                      args.name,
                      args.flip,
                      args.augmentation,
                      args.gray,
                      args.green,
                      args.binary)


if __name__ == "__main__":
    main()