import os.path as path
class file_operation(object):


    def read_file(self):
        # file name in same directory
        file_name = 'HelloWorld.py'

        if not path.isfile(file_name):
            print("file does not exist")
        else:
            # read the lines in files
            with open(file_name) as f:
                content = f.read().splitlines()

            # print the content line by line
            for line in content:
                print(line)

    def write_file(self):
        file_name = 'New_file.txt'
        # open the file name for writing
        myFile = open(file_name, 'w')
        # write the content in to file
        myFile.write("This is new content in the file")
        # close the file
        myFile.close()


    def append_file(self):
        file_name = 'New_file.txt'
        # open the file name for writing
        myFile = open(file_name, 'a')
        # write the content in to file
        myFile.write("\nThis is second line of content in the file")
        # close the file
        myFile.close()

if __name__ == '__main__':
    reading = file_operation()
    #reading.read_file()
    reading.write_file()
    reading.append_file()