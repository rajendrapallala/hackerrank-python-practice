
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
rx='^((4|5|6)[0-9]{3}(-)?([0-9]{4})(-)?([0-9]{4})(-)?([0-9]{4}))$'
rpt = r'([0-9]{1})(-)?\1(-)?\1(-)?\1'
crds = [input().strip() for _ in range(int(input()))]
'''
cs = ['3695-7963-  5827-75',
'4143-4672-8798-2968-2968',
'6865---------------3965---------------1564-------------2918',
'6865396515642918']
'''
for crd in crds[:]:
    if re.match(rx,crd):
        if re.search(rpt, crd):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')
'''
for crd in cs[:]:
    if re.match(rx,crd):
        if re.search(rpt, crd):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')
'''
