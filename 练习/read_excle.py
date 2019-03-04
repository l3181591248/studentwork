import xlrd

from framwork.logger import Logger

logger = Logger(logger="Read_excel").getlog()


class Read_excel(object):
    @classmethod
    def read_excel(self, excelpath, sheetName="Sheet1"):
        # 读取Excel表格内容       先读行 再读列   以字典方式进行数据存储
        workbook = xlrd.open_workbook(excelpath)
        sheet = workbook.sheet_by_name(sheetName)
        keys = sheet.row_values(0)  # 获取第一个key值
        rownum = sheet.nrows  # 获取总行数
        clonum = sheet.ncols  # 获取总列数
        if rownum <= 1:
            logger.error("excel表中数据总行数小于1")
        else:
            r = []
            for i in range(1, rownum):
                sheet_data = {}
                values = sheet.row_values(i)
                for j in range(clonum):
                    sheet_data[keys[j]] = values[j]
                r.append(sheet_data)
        return r


if __name__ == "__main__":
    print(Read_excel().read_excel("yingyingy.xlsx", "Sheet1"))
