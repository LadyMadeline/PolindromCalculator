# database

respond = []


# data access layer

def push_palindrome(number):
    respond.append(number)


def get_palindrome():
    return respond


# business layer

def get_respond():
    return get_palindrome()


def get_palindrome_of_number(num):
    result = num
    if result == int(str(result)[::-1]):
        return result

    while True:
        if result == int(str(result)[::-1]):
            return result

        result = result + int(str(result)[::-1])


def calculate_palindrome(number):
    for num in range(1, number + 1):
        palindrome = get_palindrome_of_number(num)
        push_palindrome('Polindrom of ' + str(num) + ' is ' + str(palindrome))

    return get_respond()


# presentation layer

def main():
    try:
        user_input_number = int(input("Enter a number: "))
        result = calculate_palindrome(user_input_number)
        for i in result:
            print(i)

    except ValueError as ex:
        print("Error: " + str(ex))

    except Exception as ex:
        print("Error: " + str(ex))


main()
