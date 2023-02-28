KEY = "03102023"

if __name__ == "__main__":
    text = "1.17.23.09.14 19.19.24.01.21.06"
    text = "19.19.19.1.27 1.22 22.16.15.10.20.21 2.17.26.12"
    words = text.split(" ")
    idx = 0
    for word in words:
        for letter in word.split("."):
            letter = int(letter)
            letter -= int(KEY[idx%len(KEY)])
            print(chr(letter+64), end="")
            idx += 1
        print("", end=" ")
        
