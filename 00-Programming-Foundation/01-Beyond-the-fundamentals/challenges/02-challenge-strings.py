miles = input('Enter a distance in miles: ')

# kilometers_value = miles_value * 1.609344
miles_as_float = float(miles)
kilometers = miles_as_float * 1.609344
results_message = 'The value in kilometers is: '

# printing the results:
print(results_message, kilometers)