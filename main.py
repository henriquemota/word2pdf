import fnmatch
from os import getcwd, path, walk

from docx2pdf import convert

root_folder = path.join(getcwd(), 'arquivos')

for root, dirnames, files in  walk(root_folder): 
	for filename in fnmatch.filter(files, '*.docx'):
		convert(path.join(root, filename), keep_active=False)
		print(f"arquivo {root}{filename} convertido")

print("Conversão realizada sucesso.")
