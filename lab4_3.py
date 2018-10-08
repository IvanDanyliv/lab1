#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import decimal
wage = decimal.Decimal(input('Введіть місячний дохід:'))
p_tax = decimal.Decimal('0.18')
m_tax = decimal.Decimal('0.015')

full_tax = wage * (p_tax + m_tax)

print('Сума податку складає: ' + str(full_tax))
