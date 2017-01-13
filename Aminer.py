import xlrd
def readexcel(name,sheet=0):
    data = xlrd.open_workbook(name)
    table = data.sheets()[sheet]
    nrows = table.nrows
    ncols = table.ncols
    ctype = 1
    xf = 0
    return table

def is_injournal(kanming):
    journal=['transaction','transactions','journal']
    for item in journal:
        if item in kanming.lower():
            return True
    return False

def is_inconf(kanming):
    conf=['conference','symposium','proceedings','workshop']
    for item in conf:
        if item in kanming.lower():
            return True
    return False

if __name__ == '__main__':
    table=readexcel('Aminer_origin.xlsx')
    j=open('journal.csv','w')
    c=open('conference.csv','w')
    un=open('undecided.csv','w')
    for i in range(1,1000):
        shortname=table.cell(i,2).value

        kanming=table.cell(i,1).value
        if not kanming:
            kanming='null'
        if is_inconf(kanming) and not is_injournal(kanming):
            c.write(kanming + '"' + shortname+'\n')
        elif not is_inconf(kanming) and is_injournal(kanming):
            j.write(kanming + '"' + shortname+'\n')
        else:
            un.write(kanming + '"' + shortname+'\n')
    j.close()
    c.close()
    un.close()
