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
        
        match comm: 
            case "-c":
                encoded_bytes = file('utf-8')
                print("Number of bytes: ", len(encoded_bytes))
            case "-l":
                print("Number of lines: ", len(file.split('\n')))
            case "-w":
                print("Number of words: ", len(file.split(' ')))
            case _:
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