# -*- coding: utf-8 -*-
import mills


class PassWdCrackOb(object):
    """
    Password cracking data object
    """

    def __init__(self,
                 service="",
                 src_ip="", src_port=0,
                 dst_ip="", dst_port=0,
                 crack_result=-1,
                 crack_detail="",
                 ts_start=0.0, ts_end=0.0,
                 ts_duration=0.0
                 ):
        """
        :param service: protocol service, such as mysql
        :param src_ip: source ip address
        :param src_port: source port address
        :param dst_ip: destination ip address
        :param dst_port: destination port address
        :param crack_result:
        1: success
        2: fail
        3: unknown error
        :param crack_detail:
        :param ts_start: start time
        :param ts_end: end time
        :param protocolconf: protocol configuration
        """
        self.service = service
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.crack_result = crack_result
        self.crack_detail = crack_detail

        self.ts_start = ts_start
        self.ts_end = ts_end

        if ts_duration == 0.0:
            self.ts_duration = self.ts_end - self.ts_start

    def toDict(self):
        """
        class instance object 2 dict
        :return:
        """
        return mills.classinstance2dict(self)
