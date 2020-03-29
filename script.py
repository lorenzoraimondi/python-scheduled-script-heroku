import time

def main():
    """
    This is the fuction triggered by the scheduler according to the cron string. 
    
    Write here your code.
    """
    
    print("Hey, I'm running stuff right now...")
    time.sleep(3)
    print("Finished! See you later!")