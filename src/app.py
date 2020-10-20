from src.product.product import get_data_using_asin

asin_number = '108127316X'


def main():
    print(get_data_using_asin(asin_number))


if __name__ == '__main__':
    main()
