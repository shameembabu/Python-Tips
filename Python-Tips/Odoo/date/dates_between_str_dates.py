# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields


def dates_between_str_dates(date1, date2, mode='date'):
    """Returns list of all dates between two string dates"""

    date_from = fields.Date.from_string(date1)
    date_to = fields.Date.from_string(date2)

    delta = date_to - date_from

    if delta.days < 0:
        return None

    res = []

    for n in range(delta.days + 1):
        if mode == 'date':
            res.append(date_from + timedelta(days=n))

        if mode == 'string':
            res.append(fields.Date.to_string(date_from + timedelta(days=n)))

    return res


