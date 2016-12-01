#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Utils():
    @staticmethod
    # dic2 keys overrides dic1 keys
    def new_dic(dic1, dic2):
        result = dict(dic1)
        print json.dumps(result)
        for key, value in dic2.iteritems():
            result[key] = value
        return result
