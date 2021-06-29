from c import NameTooShortError, InvalidDomainError, MustContainAtSymbolError

command = input()


while not command == "End":
    if command.find('@') == -1:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, extension = command.split("@")
        domain = extension.split(".")[1]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in ["com", "bg", "org", "net"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    command = input()
