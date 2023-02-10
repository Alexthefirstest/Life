from source.file_logger import logg_exception_and_print_message


@logg_exception_and_print_message
def aaaaaaa():
    print('hi')
    raise Exception('aaaaaaaa')


aaaaaaa()
