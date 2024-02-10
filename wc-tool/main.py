import cmd

class ccwc(cmd.Cmd):
  
    prompt=">>"
    intro="Welcome to the CCWC shell."
    
    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World", line)
        
    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
    def do_ccwc(self, line):
        comm, fileName = line.split()
        file = self.__readFile(fileName)
        # print(file)
        
        if comm == "-c": 
                print("Number of bytes: ", len(file))
        elif comm == "-l":
                print("Number of lines: ", len(file.split('\n')))
        elif comm == "-w":
                print("Number of words: ", (file.split(' '))) # 58164
        elif comm == "-m":
                print("Number of characters: ", (file.replace(" ", "")))
        elif comm ==  _:
                print("Unknown command")

if __name__ == '__main__':
    ccwc().cmdloop()