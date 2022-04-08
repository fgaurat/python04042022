def main():
    with open(f'le_fichier.txt','a') as f:
        print("Hello 2",file=f)
        # f.write("Hello\n")

    with open('le_fichier.txt','r') as f:
        # lines = f.readlines()

        for line in f:
            print(line.strip())
    

if __name__ == '__main__':
    main()