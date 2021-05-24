

def append_ipv4s(file):
    with open(file) as f:
        a = set()
        lines = f.read().splitlines()
        print("[*] In the file '{}', we have these ips".format(file))

        for i in lines:
            print(i)
            a.add(i)
        
    return a
    #print("_______________________________________________")


if __name__ == "__main__":
    set_a = append_ipv4s('ipa.txt')
    set_b = append_ipv4s('ipb.txt')
    print(set_a, set_b)
    list_difference= set_b -set_a
    print(list_difference)