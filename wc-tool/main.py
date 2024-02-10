import cmd

class ccwc(cmd.Cmd):
    prompt = ">>"
    intro = "Welcome to ccwc tool. Type help for available commands."
    
    def __readFile(self, fileName):
        try:
            with open(fileName) as f:
                return f.read()
        except FileNotFoundError:
            print(f"The file {fileName} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def do_hello(self,line):
        """Print a greeting"""
        print("Hello World")

    def do_quit(self, line):
        """Exit the cli"""
        return True  
    
    def do_ccwc(self, line):
        command, fileName = line.split(" ")
        file = self.__readFile(fileName)
        if command == "-c":
            print("number of bytes: ", len(file))
        if command == "-l":
            lineCount = file.count("\n")
            print("The number of lines: " , lineCount)
        if command == "-w":
            wordCount = file.count(" ")
            print("The number of words:", wordCount)
                 

if __name__ == '__main__':
    ccwc().cmdloop()