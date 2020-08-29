# -*- coding: utf-8 -*-
# @Time     : 2020/8/29-15:25
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : rever_link.py
# @Project  : Happy-Algorithm

class LinkList(object):
    def rever_list(self):
        pre = link
        cur = link.next
        pre.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre


if __name__ == '__main__':
    link = LinkList()
    link_data = [1, 2, 3, 4]
    link.rever_list(link_data)
