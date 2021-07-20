import cmd


class HelloWorld(cmd.Cmd):

    def do_greet(self, line):
        
        ''' Ayuda Please Para 
        el Metodo greet
        do_greet[line] '''
        
        print("\033[1;31;40m"+"Python Te Da La Bienvenida ", line)
        
    

    def do_EOF(self, line):
        return True
        
       


if __name__ == '__main__':
    HelloWorld().cmdloop()