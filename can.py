# -*- coding: utf-8 -*-
# !/usr/bin/python3

# can-stub

import interface


class Message:

    def __init__(self, arbitration_id, data, extended_id):
        self.arbitration_id = arbitration_id
        self.data = data
        self.extended_id = extended_id


interface.stub()
