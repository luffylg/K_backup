import re

from Aminer import readexcel
def filter(target):
    target=target.strip().replace('：',':').replace('（','(').replace('）',')').replace('"','')
    # pattern1=re.compile(r'.+?:')
    # target=re.sub(pattern1,'',target)

    pattern2=re.compile(r'\(.+?\)')
    pattern3=re.compile(r'\(.+')
    target=re.sub(pattern2,'',target)
    target = re.sub(pattern3, '', target)
    return target

def get_alpha(s):
    return ''.join([a for a in s if a.isalpha()])

def get_alpha2(s):
    return ''.join(re.findall(r'[a-zA-Z]',s))

def clear_repeat():
    journal=readexcel('total.xlsx',0)
    conference = readexcel('total.xlsx', 1)
    j=[]
    c=[]
    for i in range(1,journal.nrows):
        kanming = filter(journal.cell(i, 0).value)
        if get_alpha2(kanming.lower()) not in [get_alpha2(s.lower()) for s in j]:
            j.append(kanming)

    for i in range(1,conference.nrows):
        kanming = filter(conference.cell(i, 0).value)
        if get_alpha2(kanming.lower()) not in [get_alpha2(s.lower()) for s in c]:
            c.append(kanming)
    # for i in range(1, conference.nrows):
    #     kanming = filter(conference.cell(i, 0).value)
    #     if kanming.lower() not in [s.lower() for s in c] and get_alpha2(kanming) in [get_alpha2(s) for s in c]:
    #         print(kanming)
    return j,c

if __name__ == '__main__':
    j = open('journal.csv', 'w')
    c = open('conference.csv', 'w')
    journal,conf=clear_repeat()
    for item in journal:
        j.write(item+'\n')
    for things in conf:
        c.write(things+'\n')
    j.close()
    c.close()
    # target='International Symposium on Low Power Design（？？查与56同否？）'
    #
    # print(filter(target))