def gcd(p,q):
  if q==0:
    return p; 
  else:
    return gcd(q,p%q);


def main():
    p = int(sys.argv[1]) 
    q = int(sys.argv[2])
    divisor = gcd(p, q)
    stdio.writeln(divisor)

if __name__ == '__main__':
    main()
