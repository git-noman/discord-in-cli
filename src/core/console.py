class Console:
    @staticmethod
    def run() -> None:
        """ This function runs the console.
        Warning: this will block the thread/program if not run properly.
        """
        while True:
            command = input("> ")
            if command in ["q", "quit"]:
                break