def filter_long_names(names):
    return [name for name in names if len(name) > 8]

faculty_names = ['Pritam','Avinash','Sameer','Parthpatil']

long_names = filter_long_names(faculty_names)

print("Faculty names with more than 8 characters:", long_names)
