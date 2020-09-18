"""
对象赋值，浅拷贝，深拷贝分析

"""
import copy


will = ["Will", 28, ["Python", "C#", "JavaScript"]]

class TestFun():

    def test_fuzhi(self):
        """
        赋值：其实就是对象的引用（别名）,都指向同一个对象。不改变对象的值和内存地址。
        :return:
        """
        bett = will

        print("will=",will)
        print("对象will的内存地址=", id(will))
        for ele in will:
            print("will对象中的每个元素的内存地址=",id(ele))

        print("bett=",bett)
        print("对象bett的内存地址=",id(bett))
        for ele in bett:
            print("bett对象中的每个元素的内存地址=",id(ele))

        print("----------------修改will的值--------------------------------------------------------------------------")
        will[0] = "Wilber"
        will[2].append("CSS")
        print("will=",will)
        print("对象will的内存地址=", id(will))
        for ele in will:
            print("will对象中的每个元素的内存地址=",id(ele))

        print("bett=",bett)
        print("对象bett的内存地址=",id(bett))
        for ele in bett:
            print("bett对象中的每个元素的内存地址=",id(ele))

    def test_copy(self):
        """
        浅拷贝：拷贝父对象，不会拷贝对象的内部的子对象，will和bett是各自独立的对象，内存地址不一样，他们的子对象都引用同一个对象。
        :return:
        """
        bett = copy.copy(will)

        print("will=", will)
        print("对象will的内存地址=", id(will))
        for ele in will:
            print("will对象中的每个元素的内存地址=", id(ele))

        print("bett=", bett)
        print("对象bett的内存地址=", id(bett))
        for ele in bett:
            print("bett对象中的每个元素的内存地址=", id(ele))

        print("----------------修改will的值--------------------------------------------------------------------------")
        will[0] = "Wilber"
        will[2].append("CSS")
        print("will=",will)
        print("对象will的内存地址=", id(will))
        for ele in will:
            print("will对象中的每个元素的内存地址=",id(ele))

        print("bett=",bett)
        print("对象bett的内存地址=",id(bett))
        for ele in bett:
            print("bett对象中的每个元素的内存地址=",id(ele))

    def test_deep_copy(self):
        """
        深拷贝：完全拷贝了父对象及其子对象，两者是完全独立的。
        :return:
        """
        bett = copy.deepcopy(will)

        print("will=", will)
        print("对象will的内存地址=", id(will))
        for ele in will:
            print("will对象中的每个元素的内存地址=", id(ele))

        print("bett=", bett)
        print("对象bett的内存地址=", id(bett))
        for ele in bett:
            print("bett对象中的每个元素的内存地址=", id(ele))

        print("----------------修改will的值--------------------------------------------------------------------------")
        will[0] = "Wilber"
        will[2].append("CSS")
        print("will=",will)
        print("对象will的内存地址=", id(will))
        for ele in will:
            print("will对象中的每个元素的内存地址=",id(ele))

        print("bett=",bett)
        print("对象bett的内存地址=",id(bett))
        for ele in bett:
            print("bett对象中的每个元素的内存地址=",id(ele))



TestFun().test_deep_copy()