import random;
def password():
    z = ""
    n = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_-+={}[]|;',./~``'"
    for x in range(0,10):
        i = random.randint(0,len(n)+1);
        z = z + n[i:i+1];
    return z;
def main():
    print(password());
    print(password());
main();
x = 2;
