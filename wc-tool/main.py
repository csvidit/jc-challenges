import cmd

class CCWC(cmd.Cmd):
    
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
                
    def __readFile(self, fileName):
        try: 
            with open(fileName) as f:
                return f.read()
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print("Error: ", e)
            return None
            

if __name__ == '__main__':
    CCWC().cmdloop()