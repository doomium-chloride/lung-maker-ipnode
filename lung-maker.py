import sys
from decimal import Decimal

basis_folder = "basis/"
file_end = ".ipnode"

def read_lung(num, left):
	base = "fittedLeft-" if left else "fittedRight-"
	
	if num == 0:
		w = "000"
	elif num == 1:
		w = "100"
	elif num == 2:
		w = "010"
	elif num == 3:
		w = "001"
	else:
		raise ValueError("num must be an int between 0 and 3")
	
	lung_fileName = basis_folder + base + w + file_end
	
	with open(lung_fileName, 'r') as file:
		return file.read()

def load_lung(num, left):
	lung_text = read_lung(num, left)
	lung_lines = lung_text.splitlines()
	return lung_lines
		
def make_base_text(data):
	lines = []
	dynamic = []
	for line in data:
		if "coordinate is" in line:
			dynamic.append(True)
			temp = line.split(' ')[:-1]
			temp = ' '.join(temp)
			lines.append(temp)
		elif "The derivative wrt direction" in line:
			dynamic.append(True)
			temp = line.split(' ')[:-1]
			temp = ' '.join(temp)
			lines.append(temp)
		else:
			dynamic.append(False)
			lines.append(line)
	return lines, dynamic

def combine(weights, values):
	v0 = values[0]
	v = []
	for i in range(1, 4):
		diff = values[i] - v0
		weighted = weights[i - 1] * diff
		v.append(weighted)
	return v0 + sum(v)

def get_value(line):
	words = line.split()
	num = words[-1]
	return Decimal(num)
	
def extract_values(w0, w1, w2, w3, i):
	v0 = get_value(w0[i])
	v1 = get_value(w1[i])
	v2 = get_value(w2[i])
	v3 = get_value(w3[i])
	return (v0, v1, v2, v3)

def make_line(base_text, value, i):
	temp = (base_text[i], str(value))
	return ' '.join(temp)

def process(weights, left):
	w0 = load_lung(0, left)
	w1 = load_lung(1, left)
	w2 = load_lung(2, left)
	w3 = load_lung(3, left)
	base_text, dynamic = make_base_text(w0)
	output = []
	for i in range(len(dynamic)):
		if(dynamic[i]):
			values = extract_values(w0, w1, w2, w3, i)
			value = combine(weights, values)
			text = make_line(base_text, value, i)
			output.append(text)
		else:
			text = base_text[i]
			output.append(text)
	return output

def list2text(array):
	return '\n'.join(array)
	
def generate_filename(prepend, left, weights):
	weight_text = ""
	for weight in weights:
		temp = "-" + str(weight)
		weight_text += temp
	if prepend != "":
		prepend += "-"
	main_text = "left" if left else "right"
	return prepend + main_text + weight_text + file_end

def write2file(filename, text):
	with open(filename, 'w') as file:
		file.write(text)

weights = (Decimal(sys.argv[1]), Decimal(sys.argv[2]), Decimal(sys.argv[3]))

print("weights are {0}, {1}, {2}".format(str(weights[0]), str(weights[1]), str(weights[2])))

output_name = sys.argv[4] if len(sys.argv) >= 5 else ""

left_list = process(weights, True)

right_list = process(weights, False)

left_text = list2text(left_list)

right_text = list2text(right_list)

left_filename = generate_filename(output_name, True, weights)

right_filename = generate_filename(output_name, False, weights)

write2file(left_filename, left_text)

write2file(right_filename, right_text)

fin = "saved to {0} and {1}".format(left_filename, right_filename)

print(fin)