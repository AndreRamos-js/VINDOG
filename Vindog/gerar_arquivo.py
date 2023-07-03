import os

def get_files(directory):
    file_list = []
    source_dirs = ['settings', 'celery', 'urls', 'forms', 'models', 'tasks', 'views', 'templates']  # Diretórios relevantes para o código fonte

    for root, dirs, files in os.walk(directory):
        # Ignorar diretórios específicos
        dirs[:] = [d for d in dirs if d not in ['env', 'migrations', 'cache']]

        for file in files:
            filepath = os.path.join(root, file)

            # Incluir arquivos relevantes do código fonte e templates
            if (any(dir_name in filepath for dir_name in source_dirs) and file.endswith('.py')) or file.endswith('.html'):
                file_list.append(filepath)
    
    return file_list

def save_file_list(file_list, output_file):
    with open(output_file, 'w') as file:
        for filepath in file_list:
            with open(filepath, 'r') as source_file:
                file.write(f"File: {filepath}\n")
                file.write(source_file.read())
                file.write("\n\n")

# Diretório raiz da sua aplicação Python
app_directory = "C:\\Users\\andre\\OneDrive\\Documentos\\GitHub\\VINDOG\\Vindog"

# Nome do arquivo de saída
output_file = "arquivos.txt"

files = get_files(app_directory)
save_file_list(files, output_file)
