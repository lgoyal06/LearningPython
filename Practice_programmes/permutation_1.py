def permutation(depth, prefix,suffix):
    if len(suffix)==0:
        return print(prefix)
    else:
        for i in range(0,len(suffix)):
            next_prefix=prefix + [suffix[i]]
            next_suffix=suffix[0:i]+suffix[i+1:]
            tab(depth)
            print(next_prefix, next_suffix, sep=':')
            permutation(depth+1, next_prefix,next_suffix)

def tab(n):
    for i in range(n):
        print(end=' ')
    
def main():
    permutation(0,[],[1,2,3,4])

main()
    
    
