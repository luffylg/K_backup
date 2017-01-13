from Aminer import readexcel
from total import get_alpha2
from total import filter
def handle_target(s):
    s=filter(s)

def get_target():
    j_target=readexcel('信息与电子工程学部 期刊（已明确）.xlsx')
    c_target=readexcel('信息与电子工程学部 会议（已明确）.xlsx')
    j_list=[]
    c_list=[]
    for i in range(0,j_target.nrows):
        kanming = j_target.cell(i, 1).value.strip()
        if kanming not in j_list:
            j_list.append(kanming)
    for i in range(0,c_target.nrows):
        kanming = c_target.cell(i, 2).value.strip()
        if kanming not in c_list:
            c_list.append(kanming)
    print(len(j_list))
    print(len(c_list))
    return j_list,c_list


def inside(item, list):
    if not list:
        return False
    for things in list:
        if item in things:
            return True
    return False


if __name__ == '__main__':
    journal = readexcel('compare.xlsx', 0)
    conference = readexcel('compare.xlsx', 1)
    j = open('journal.csv', 'w')
    c = open('conference.csv', 'w')
    j_list, c_list=get_target()
    for i in range(1, journal.nrows):
        kanming = journal.cell(i, 0).value.strip()
        if not inside(get_alpha2(kanming.lower()),[get_alpha2(s.lower()) for s in j_list]):
        # if get_alpha2(kanming.lower()) not in [get_alpha2(s.lower()) for s in j_list]:

            j.write(kanming + '\n')
            j_list.append(kanming)

    for i in range(1, conference.nrows):
        kanming = conference.cell(i, 0).value.strip()
        if not inside(get_alpha2(kanming.lower()),[get_alpha2(s.lower()) for s in c_list]):
            c.write(kanming + '\n')
            c_list.append(kanming)

    j.close()
    c.close()