#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # get all the names defined in the module
    module_names = dir(hidden_4)

    # filter out names beginning with an underscore

    filter_names = [name for name in module_names if not name.startswith('_')]

    # print the filtered names, one per line
    for name in filter_names:
        print(name)
