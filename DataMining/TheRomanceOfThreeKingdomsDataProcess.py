import jieba
import re
import jieba.posseg as pseg


class TheRomanceOfThreeKingdomsDataPreprocessing:
    def dataPreprocessing(self):

        excludes = {'将军', '却说', '令人', '赶来', '徐州', '不见', '下马', '喊声', '因此', '未知', '大败', '百姓', '大事', '一军', '之后', '接应',
                    '起兵', '成都', '原来', '江东', '正是', '忽然', '原来', '大叫', '上马', '天子', '一面', '太守', '不如', '忽报', '后人', '背后',
                    '先主',
                    '此人', '城中', '然后', '大军', '何不', '先生', '何故', '夫人', '不如', '先锋', '二人', '不可', '如何', '荆州', '不能', '如此',
                    '主公',
                    '军士', '商议', '引兵', '次日', '大喜', '魏兵', '军马', '于是', '东吴', '今日', '左右', '天下', '不敢', '陛下', '人马', '不知',
                    '都督',
                    '汉中', '一人', '众将', '后主', '只见', '蜀兵', '马军', '黄巾', '立功', '白发', '大吉', '红旗', '士卒', '钱粮', '于汉', '郎舅',
                    '龙凤',
                    '古之', '白虎', '古人云', '尔乃', '马飞报', '轩昂', '史官', '侍臣', '列阵', '玉玺', '车驾', '老夫', '伏兵', '都尉', '侍中', '西凉',
                    '安民',
                    '张曰', '文武', '白旗', '祖宗', '寻思'}  # 排除的词汇

        with open('../processingData/threeKingdoms.txt', 'r', encoding='UTF-8') as novelFile:
            novel = novelFile.read()
        novelList = re.split(r'([。？！])', novel)
        recordList = []
        # print(novelList)

        # 针对每一句话进行处理，去除掉不需要的符号
        for item in novelList:
            if item != '\n' and item != ' ' and item != '' and item != '。' and item != '\u3000' and item != '！':
                item = item.replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
                recordList.append(item)
        print("*********************************************************************************")
        # print(recordList)
        # 导入停词文件
        stopwords = [line.strip() for line in open('../stop.txt', 'r', encoding='UTF-8').readlines()]
        # 每一句话去除停词以及需要排除的词三国里面的词
        temp = []
        result = []
        for record in recordList:
            k = pseg.cut(record, use_paddle=True)
            for i in k:
                if i.word in stopwords or i.word in excludes or len(i.word) < 2 or (
                        i.flag == 'nr' and i.flag != 'nz' and i.flag != 'n' and i.flag != 'ns'):
                    continue
                elif i.word == '孔明' or i.word == '孔明曰' or i.word == '卧龙先生':
                    i.word = '诸葛亮'  # 把相同意思的名字归为一个人
                elif i.word == '云长' or i.word == '关公曰' or i.word == '关公':
                    i.word = '关羽'
                elif i.word == '玄德' or i.word == '玄德曰' or i.word == '玄德甚' or i.word == '玄德遂' or i.word == '玄德兵' or i.word == '玄德领' \
                        or i.word == '玄德同' or i.word == '刘豫州' or i.word == '刘玄德':
                    i.word = '刘备'
                elif i.word == '孟德' or i.word == '丞相' or i.word == '曹贼' or i.word == '阿瞒' or i.word == '曹丞相' or i.word == '曹将军':
                    i.word = '曹操'
                elif i.word == '高祖':
                    i.word = '刘邦'
                elif i.word == '光武':
                    i.word = '刘秀'
                elif i.word == '桓帝':
                    i.word = '刘志'
                elif i.word == '灵帝':
                    i.word = '刘宏'
                elif i.word == '公瑾':
                    i.word = '周瑜'
                elif i.word == '伯符':
                    i.word = '孙策'
                elif i.word == '吕奉先' or i.word == '布乃' or i.word == '布大怒' or i.word == '吕布之':
                    i.word = '吕布'
                elif i.word == '赵子龙' or i.word == '子龙':
                    i.word = '赵云'
                elif i.word == '卓大喜' or i.word == '卓大怒':
                    i.word = '董卓'  # 把相同意思的名字归为一个人
                temp.append(i.word)
            if temp:
                result.append(temp)
                # print(temp)
            temp = []
        recordList = result
        # print(recordList)
        lenRecordList = len(recordList)
        processedData = {}

        for k in range(lenRecordList):
            processedData[k] = recordList[k]
        # 下面输出预处理后的数据
        # print(processedData)
        # with open('../ProcessedData/processedThreeKingdoms.txt', 'w', encoding='UTF-8') as processedDataFile:
        #     for key, value in processedData.items():
        #         processedDataFile.write(str(key))
        #         processedDataFile.write(': ')
        #         processedDataFile.write(str(value))
        #         processedDataFile.write(str('\n'))
        return processedData


#
# a = TheRomanceOfThreeKingdomsDataPreprocessing()
# a.dataPreprocessing()
# str = '邓艾\n\u3000\u3000部将见钟会已死，就飞马去追救邓艾'
# str = str.replace(u'\u3000',u'').replace('\n', '').replace('\r', '').replace(" ","")
# print(str)
