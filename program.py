import os
import cat_service


def main():
    print_header()
    folder = do_output_folder()
    # get/create output folder
    # download cats
    # display cats


def print_header():
    print('----------------------------')
    print('         CAT FACTORY')
    print('----------------------------')


def do_output_folder():
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join('.', folder))
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating directory {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_service.get_cat(folder, '')


if __name__ == '__main__':
    main()


