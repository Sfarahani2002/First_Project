import re

#region dot

# dot (.)
# text = 'this is fun'
# if re.search('f.n', text):
#     print('this is ok')
#
#endregion

#region ^
#
# text = 'Toplearn'
# if re.search('^Top', text):
#     print('this is ok')

#endregion

# region$

# text = 'Toplearn'
# if re.search('rn$', text):
#     print('this is ok')

# endregion

# region escape
# text = 'this is a book.'
# if re.search('book\.', text):
#     print('this is ok')

#endregion

# region set
#
# text = 'site'
# if re.search('si[tdz]e', text):
#     print('this is ok')
#
#endregion

#region range

# text ='s'
# if re.search('[a-zA-Z]',text):  # [0-9][a-z]
#     print('this is ok')
# endregion

#region exclude

# text = 'siue'
# if re.search('si[^tsz]e', text):
#     print('this is ok')
#
# endregion

#region repeat

# text = '09123456789'
# if re.search('[0-9]{11}', text):
#     print('this is ok')
#
# endreigion

