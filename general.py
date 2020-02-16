import os


# Each website is a separate project (folder)
#only creating directory if is not created before
#os.makedirs created the directory
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
#creating queue and crawled files inside project directory & 1st queue need base url
#queue is the path to the queue.txt file & same as for crawled
#os.path.isfile is checking whether the file already exist or not
#write_file is following the function below
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
#with open is opening the file to write in it and closing it after writing it
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
#a means files is in append mode
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
#when file is open it gonna iterate through each line in the file as rt mode which is reading the file in text mode
#in  set it going to add and replace the new line and store all the result in set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate through a set, each item will be a line in a file
#storing the set results in file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")