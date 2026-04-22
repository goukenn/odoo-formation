class cli:
    """
    CLI helper to render color 
    """
    reset = "\033[0m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"


    @staticmethod
    def Red(text: str) -> str : 
        return cli.red+ text + cli.reset 
        
    @staticmethod
    def Green(text: str) -> str : 
        return cli.green+ text + cli.reset 
     
    @staticmethod
    def Yellow(text: str) -> str : 
        return cli.yellow+ text + cli.reset 
 
    @staticmethod
    def Blue(text: str) -> str : 
        return cli.blue+ text + cli.reset 