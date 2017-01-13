from Aminer import readexcel
from total import filter


if __name__ == '__main__':
    table=readexcel('Aminer 期刊、会议列表   分类（初步）--蔡来.xlsx',3)
    # target=readexcel('compare.xlsx',1)
    doc=open('doc.csv','w')
    for i in range(0,table.nrows):
        kanming = filter(table.cell(i, 0).value)
        doc.write(kanming+'\n')
    doc.close()