import os

def Find_files(suffix, path):
	"""
	Find all files beneath path with file name suffix.
	Note that a path may contain further subdirectories
	and those subdirectories may also contain further subdirectories.
	There are no limit to the depth of the subdirectories can be.
	Args:
	suffix(str): suffix if the file name to be found
	path(str): path of the file system
	Returns:
	a list of paths
	"""
	if not os.path.isdir(path):
		 return 'Invalid Directory'

	path_list = os.listdir(path)
	output = []
	for item in path_list:
		item_path = os.path.join(path, item)
		if os.path.isdir(item_path):
			output += Find_files(suffix,item_path)
		if os.path.isfile(item_path) and item_path.endswith(suffix):
			output.append(item_path)
	return output

# # Test case 1
# print(find_files('.c', './Problem 2/testdir'))
# # Test case 2
# print(find_files('.c', './asdf'))
# print(find_files('.c', './Problem 2/emptydir'))
# # Test case 3
# print(find_files('', './Problem 2/testdir'))
# print(find_files('.z', './Problem 2/testdir'))/

#Test Case1            
Referance_Path = os.getcwd() + '/testdir'
print(Find_files('.c',path=Referance_Path))
print("///////////////////////////////////////////////////////////////////////")

#Test Case2            file not in path
Referance_Path = "C:/Users/gasse/OneDrive/Desktop"
print(Find_files('.c',path=Referance_Path))#takes longer because has to search all files and folders in desktop 
print("///////////////////////////////////////////////////////////////////////")

# Test Case3           path doesnt exist
Referance_Path = '/testdir'
print(Find_files('.c',path=Referance_Path))
print("///////////////////////////////////////////////////////////////////////")