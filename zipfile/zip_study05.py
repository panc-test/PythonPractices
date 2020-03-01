'''
ZipInfo类，是存储的zip文件的每个文件的信息

ZipFile.getinfo(name)   功能：获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息。将在下面 具体介绍该对象。
ZipFile.infolist()  功能：获取zip文档内所有文件的信息，返回一个zipfile.ZipInfo的列表。

'''

# importing required modules
from zipfile import ZipFile
import datetime

# specifying the zip file name
file_name = 'new.zip'

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    for info in zip.infolist():
            print(info.filename)
            print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
            print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)')
            print('\tZIP version:\t' + str(info.create_version))
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes')



'''
拓展：
ZipInfo.filename： 获取文件名称。
ZipInfo.date_time： 获取文件最后修改时间。返回一个包含6个元素的元组：(年, 月, 日, 时, 分, 秒)
ZipInfo.compress_type： 压缩类型。
ZipInfo.comment： 文档说明。
ZipInfo.extr： 扩展项数据。
ZipInfo.create_system： 获取创建该zip文档的系统。
ZipInfo.create_version： 获取 创建zip文档的PKZIP版本。
ZipInfo.extract_version： 获取 解压zip文档所需的PKZIP版本。
ZipInfo.reserved： 预留字段，当前实现总是返回0。
ZipInfo.flag_bits： zip标志位。
ZipInfo.volume： 文件头的卷标。
ZipInfo.internal_attr： 内部属性。
ZipInfo.external_attr： 外部属性。
ZipInfo.header_offset： 文件头偏移位。
ZipInfo.CRC： 未压缩文件的CRC-32。
ZipInfo.compress_size： 获取压缩后的大小。
ZipInfo.file_size： 获取未压缩的文件大小。

'''




