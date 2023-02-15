import string
import random

# Run file as `python stock_number_challenge.py` (if in the directory)

example_artwork_data = [
	# Edge case with stock_number in incorrect type
	{
		"stock_number": 6,
		"title": "Untitled (Florence) 1",
		"id": 456,
		"artist": "Flora Brooke",
	},
	# Edge case with stock_number not defined
	{
		"title": "Untitled (Florence) 1",
		"id": 456,
		"artist": "Flora Brooke",
	},
	# Edge case with title not defined
	{
		"stock_number": "CJL 913",
		"id": 456,
		"artist": "Flora Brooke",
	},
	# Edge case with id not defined
	{
		"stock_number": "CJL 913",
		"title": "Untitled (Florence) 1",
		"artist": "Flora Brooke",
	},
	# Edge case with artist not defined
	{
		"stock_number": "CJL 919",
		"title": "Untitled (Florence) 1",
		"id": None,
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 1",
		"id": 456,
		"artist": "Flora Brooke",
	},
	# Added an edge case for when theres no "id" provided.
	# We can assume that this is a required field.
	{
		"stock_number": "CJL 919",
		"title": "Untitled (Florence) 1",
		"id": None,
		"artist": "Flora Brooke",
	},
	# Added an edge case for when the artist just goes by one name.
	{
		"stock_number": "JCL 121",
		"title": "My Beautiful Artwork 1",
		"id": 455,
		"artist": "Chris",
	},
	{
		"stock_number": "JCL-121",
		"title": "My Beautiful Artwork 1",
		"id": 455,
		"artist": "Chris",
	},
	# Added an edge case for when there's no artist name provided.
	{
		"stock_number": "302",
		"title": "Untitled (Florence) 2",
		"id": 354,
		"artist": "",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 10",
		"id": 465,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 11",
		"id": 466,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 12",
		"id": 467,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "003",
		"title": "Untitled (Florence) 2",
		"id": 457,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 3",
		"id": 458,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 4",
		"id": 459,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 5",
		"id": 460,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 6",
		"id": 461,
		"artist": "Flora Violet Brooke",
	},
	{
		"stock_number": "",
		"title": "Untitled (Florence) 7",
		"id": 462,
		"artist": "Flora Violet Brooke",
	},
	{"stock_number": "", "title": "Untitled (Florence) 8", "id": 463, "artist": ""},
	{"stock_number": "", "title": "Untitled (Florence) 9", "id": 464, "artist": ""},
	{
		"stock_number": "KAD 0002",
		"title": "Dubai Construction Workers 1",
		"id": 448,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "KAD 001",
		"title": "Dubai Construction Workers 2",
		"id": 447,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "",
		"title": "Dubai Construction Workers 3",
		"id": 449,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "",
		"title": "Dubai Construction Workers 4",
		"id": 450,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "",
		"title": "Dubai Construction Workers 5",
		"id": 451,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "KDA",
		"title": "Dubai Construction Workers 6",
		"id": 452,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "",
		"title": "Dubai Construction Workers 7",
		"id": 453,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "",
		"title": "Dubai Construction Workers 8",
		"id": 454,
		"artist": "Kadeem Darzi",
	},
	{
		"stock_number": "DOO 003",
		"title": "Untitled",
		"id": 621,
		"artist": "Katherine Dooley",
	},
	{
		"stock_number": "DOO 004",
		"title": "Untitled",
		"id": 622,
		"artist": "Katherine Dooley",
	},
	{
		"stock_number": "",
		"title": "Dubai Construction Workers 9",
		"id": 455,
		"artist": "",
	},
	{
		"stock_number": "",
		"title": "Pastoral Scene",
		"id": 468,
		"artist": "Thomas Dedrick",
	},
	{
		"stock_number": "",
		"title": "Pastoral Scene",
		"id": 470,
		"artist": "Thomas Dedrick",
	},
	{
		"stock_number": "",
		"title": "Pastoral Scene",
		"id": 471,
		"artist": "Thomas Dedrick",
	},
	{"stock_number": "", "title": "Stormy Seas", "id": 469, "artist": "Thomas Dedrick"},
	{
		"stock_number": "",
		"title": "Lady Cynthia Stephenson",
		"id": 472,
		"artist": "Charles Eggins",
	},
	{
		"stock_number": "",
		"title": "Pongo and Westie",
		"id": 473,
		"artist": "Charles Eggins",
	},
	{"stock_number": "", "title": "Rover", "id": 474, "artist": "Charles Eggins"},
	{
		"stock_number": "BL 001",
		"title": "Energy and serenity 1",
		"id": 440,
		"artist": "Blake Ellery",
	},
	{
		"stock_number": "BLA 004",
		"title": "Energy and serenity 2",
		"id": 441,
		"artist": "Blake Ellery",
	},
	{
		"stock_number": "",
		"title": "Energy and serenity 3",
		"id": 442,
		"artist": "Blake Ellery",
	},
	{
		"stock_number": "",
		"title": "Energy and serenity 4",
		"id": 443,
		"artist": "Blake Ellery",
	},
	{
		"stock_number": "BLA 004",
		"title": "Energy and serenity 5",
		"id": 444,
		"artist": "Blake Ellery",
	},
	{
		"stock_number": "",
		"title": "Energy and serenity 6",
		"id": 445,
		"artist": "Blake Ellery",
	},
	{
		"stock_number": "",
		"title": "Energy and serenity 7",
		"id": 446,
		"artist": "Blake Ellery",
	},
	{"stock_number": "", "title": "Relief 39", "id": 281, "artist": "Yuming Han"},
	{"stock_number": "Y", "title": "Rust 1", "id": 283, "artist": "Yuming Han"},
	{"stock_number": "", "title": "Rust 2", "id": 284, "artist": "Yuming Han"},
	{"stock_number": "ABC 022", "title": "Pineapple ", "id": 285, "artist": "Banksy"},
	{
		"stock_number": "AG-001-MET",
		"title": "Annunciation ",
		"id": 555,
		"artist": "Artemisia Gentileschi",
	},
	{
		"stock_number": "AG-002-MET",
		"title": "Aurora ",
		"id": 556,
		"artist": "Artemisia Gentileschi",
	},
]


def create_new_stock_number_prefix(artwork, return_original_stock_number=False):
	"""
	This function will take an existing artwork object, and a new
	stock number prefix will be created based on some pre-existing rules given, and
	described below.

	e.g artwork: {
		"stock_number": "003",
		"title": "Untitled (Florence) 2",
		"id": 457,
		"artist": "Flora Violet Brooke",
	}

	Parameters:
		artwork (dict): {
			stock_number (str): A string containing the stock number (optional),
			title (str): A string with the artwork title (required),
			id (int): An integer with the unique id of the artwork (required),
			artist (str): A string with the artists name (optional).
		}
		return_original_stock_number (bool): A boolean variable to return the original stock number.
																																									 default: False

	Returns:
		new_stock_number_prefix (str): String of the new stock number prefix.

	Rules:
		# Generate a new stock number 'prefix' - existing stock numbers.
		# - two-letter prefix
		# - first letter, if possible, first letter of artists first name.
		# - 2nd letter, if possible, first letter of artists last name.
		# - prefixes must be unique per artist
		# *****
		# - number: existing stock number number
		# - separator: existing separator
		# - suffix: existing suffix
		# - general: stock number must be unique
		# e.g cases
		# *****
		# - Kadeem Darzi, 'KAD 001' ----> new stock number = 'KD 001'
		# - Kadeem Darzi 'KAD 0002' ----> new stock number = 'KD 0002'
		# - James Perrogi 'JAM 001-S' ----> new stock number = 'JP 001-S'
		# *****
		# - skip artworks that have no stock numbers
		# - edge cases to consider
	"""

	stock_number = artwork.get("stock_number", "")
	name = artwork.get("artist", "")
	artist_id = artwork.get("id", "")

	if return_original_stock_number:
		return stock_number

	# First check if there is no stock number present,
	# return an empty string in this edge case
	if not stock_number or not isinstance(stock_number, str):
		return ""

	# We can assume if theres no artist id, then we can exit.
	if not artist_id or not isinstance(artist_id, int):
		return ""

	# No artist name present, this is an edge case that must be handled.
	# In this case we'll select a different letter for the prefix, a randomly
	# selected letter.
	first_letter = ""
	second_letter = ""

	if not name:
		# Ensure these are randomised per artist
		print(
			"No artist name provided, randomly selcting both letters for the prefix in this case."
		)
		first_letter = random.choice(string.ascii_uppercase)
		second_letter = random.choice(string.ascii_uppercase)

	if len(name) > 0:
		# Lets grab the different names from the artist
		names = name.split()
		print("Artist names: " + str(names))
		first_name = names[0]
		first_letter = first_name[0]

		# Check if the artist has a surname as well,
		# if not then we'll just use the last letter of their first name.
		if len(names) > 1:
			last_name = names[-1]
			second_letter = last_name[0]
		else:
			print(
				"Artist only has one name, using the last letter in their first name in this case."
			)
			second_letter = first_name[-1].upper()

	print("New Prefix: %s%s" % (first_letter, second_letter))

	return first_letter + second_letter


def create_new_stock_numbers(artwork_data):
	"""
	This function will take an existing artwork object, and a new
	stock number will be created based on some pre-existing rules given, and
	described below.

	e.g artwork: {
		"stock_number": "003",
		"title": "Untitled (Florence) 2",
		"id": 457,
		"artist": "Flora Violet Brooke",
	}

	Parameters:
	artwork (dict): {
		stock_number (str): A string containing the stock number (optional),
		title (str): A string with the artwork title (required),
		id (int): An integer with the unique id of the artwork (required),
		artist (str): A string with the artists name (optional).
	}

	Returns:
		new_stock_number (str): String of the new stock number created.

	Rules:
		# Generate a new stock number - using existing stock numbers.
		# - two-letter prefix
		# - first letter, if possible, first letter of artists first name.
		# - 2nd letter, if possible, first letter of artists last name.
		# - prefixes must be unique per artist
		# *****
		# - number: the number part must be an incrementing 3 digit number,
														specific to that artist, starting at 1, padded wiht zeros
														e.g '001', '002' etc.
		# - separator: same separator for every artist and artwork.
		# - suffix: keep existing suffix
		# - general: Every stock number must be unique
		# e.g cases
		# *****
		# - Kadeem Darzi, 'KAD 001' ----> new stock number = 'KD 001'
		# - Kadeem Darzi 'KAD 0002' ----> new stock number = 'KD 0002'
		# - James Perrogi 'JAM 001-S' ----> new stock number = 'JP 001-S'
		# *****
		# - skip artworks that have no stock numbers
		# - if we already have created a stock number for an artist, the next one
		#   should have the number 002, then 003 so increment them.
		# - edge cases to consider
	"""
	# We'll use this variable to keep track of artists we've already
	# generated stock numbers for.
	artists = {}

	# We'll use the same separator for all artists

	for artwork in artwork_data:
		stock_number = artwork.get("stock_number", "")
		title = artwork.get("title", "")
		name = artwork.get("artist", "")
		artist_id = artwork.get("id", "")

		if not name:
			# If there's no artist name provided, we can assume that we can skip this entry
			# as we can't create a new stock number in that case.
			continue

		# Create a new prefix using our earlier function.
		new_prefix = create_new_stock_number_prefix(artwork)

		if not new_prefix:
			# If there's no prefix generated i.e in the edge cases defined in
			# 'create_new_stock_number_prefix', then we'll assume an error in the data,
			# and skip this entry.
			continue

		# Check if we've already incremented a particular artists artwork,
		# if not, then add it to the dict with 1 as the starting point
		if name in artists:
			artists[name] += 1
		else:
			artists[name] = 1

		suffix = ""
		separator = " "

		if stock_number:
			if "-" in stock_number:
				separator = "-"

			stock_no_prefix = stock_number.split(separator)

			if len(stock_no_prefix) == 3:
				suffix = separator + stock_no_prefix[-1]

		# Padd the number with leading zeros up to 3 digits.
		new_stock_number = "%s%s%s%s" % (
			new_prefix,
			separator,
			str(artists[name]).zfill(3),
			suffix,
		)

		print(
			"%s: %s, %s"
			% (
				artist_id,
				name,
				title,
			)
		)
		print("Old stock number: %s" % stock_number)
		print("New stock number: %s" % new_stock_number)
		print("\n")

	print("All listed artists, and their number of artworks.")
	for artist, count in artists.items():
		print("Artist: %s, Works: %s " % (artist, str(count)))


print("\nTask 1: `create_new_stock_number_prefix`")

for example_artwork in example_artwork_data:
	print("\n=================================\n")
	print("%s" % example_artwork)
	new_prefix = create_new_stock_number_prefix(example_artwork)

	if not new_prefix:
		print("Skipped edge case.")
		continue

	print("\nfunction create_new_stock_number_prefix: %s\n" % new_prefix)
	stock_number = example_artwork.get("stock_number", "")

	if stock_number:
		separator = " "
		if "-" in stock_number:
			separator = "-"

		stock_no_prefix = stock_number.split(separator)

		if not (stock_no_prefix[0].isdigit()):
			del stock_no_prefix[0]

		new_stock_number = "%s%s%s" % (new_prefix, separator, "-".join(stock_no_prefix))
		print("New stock number: %s" % new_stock_number)
print("\n=================================\n")


# TASK 2

print("\nTask 2: `create_new_stock_numbers`")
create_new_stock_numbers(example_artwork_data)
