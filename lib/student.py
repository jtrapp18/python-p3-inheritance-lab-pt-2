class Student:

    def __init__(self):
        pass

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    
    def __init__(self):
        super().__init__()

    def hello(self):
        super().hello()

        chatter = """
        How are you doing today? I'm okay, but I'm kind of tired. Did you 
        watch The Walking Dead last night? You didn't?! Oh man, it was so 
        crazy! What, you don't want any spoilers? Okay well let me just 
        tell you who died...
        """

        print(" ".join(chatter.replace("\n", " ").split()))
        
    def raise_hand(self):
        for i in range(0, 10):
            super().raise_hand()
    

student = Student()
student.hello()
student.raise_hand()

jacqueline = ChattyStudent()
jacqueline.hello()
jacqueline.raise_hand()