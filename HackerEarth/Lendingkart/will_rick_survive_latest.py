def check(a):
        size = 6
        count = 0; i = 1; last_reload = 0
        while i < len(a):
                if a[i]:
                        reload = (count + a[i] - 1) / size
                        if count + a[i] + reload > i:
                                sieve = [0] * (reload+count+a[i])
                                sieve[size::size+1] = [1] * reload
                                #print reload, count, a[i], i, sieve, ((size+1)*last_reload)-1, i, sieve[(size+1)*last_reload:i]
                                print "Goodbye Rick"; print sieve[:i].count(0); return
                        count += a[i]
                        last_reload = reload
                i += 1
        print "Rick now go and save Carl and Judas"

def main(): 
        T = int(raw_input())
        for i in range(T): 
                n = int(raw_input())
                x = [0] * 50001
                s = [int(each) for each in raw_input().split()]
                for each in s:
                        x[each] += 1
                check(x)
main()

