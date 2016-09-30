#!/usr/bin/env python3

area_dict = {
    '湖北': {
        '武汉': ['汉口', '武昌', '汉阳'],
        '孝感': ['云梦', '安陆', '应城'],
        '宜昌': ['三峡', '兴山', '枝江']
    },
    '广东': {
        '深圳': ['南山', '福田', '罗湖'],
        '广州': ['从化', '花都', '番禺'],
        '珠海': ['斗门', '金湾', '香洲']
    },

    '浙江': {
        '杭州': ['西湖', '上城', '拱墅'],
        '宁波': ['奉化', '慈溪', '余姚'],
        '温州': ['瑞安', '文成', '乐清']
    }
}
exit_code = 1

while exit_code != 0:
    for province in area_dict:
        print('* %s' % province)
    province_input = input('请输入省份(输入“e”退出程序):')
    if province_input == 'e':
        exit_code = 0
        continue
    elif province_input in area_dict:
        while exit_code != 0:
            for city in area_dict[province_input]:
                print('* %s' % city)
            city_input = input('请输入省份(输入“e”退出程序，输入“q”返回上级菜单):')
            if city_input == 'e':
                exit_code = 0
                continue
            elif city_input == 'q':
                break
            elif city_input in area_dict[province_input]:
                while exit_code != 0:
                    for area in area_dict[province_input][city_input]:
                        print('* %s' % area)
                    area_input = input('请输入省份(输入“e”退出程序，输入“q”返回上级菜单):')
                    if area_input == 'e':
                        exit_code = 0
                        continue
                    elif area_input == 'q':
                        break
                    elif area_input in area_dict[province_input][city_input]:
                        print('欢迎来到%s' % area_input)
                        exit_code = 0
                        continue
                    else:
                        print('输入有误，请检查输入！')
            else:
                print('输入有误，请检查输入！')
    else:
        print('输入有误，请检查输入！')
