print 'Welcome! This is all of the content from Dublin High Honors Chemistry du\
ring the 2018-2019 school year in Python functions!'

# ---------------------------Unit 1 - Defining Matter---------------------------

def sig_figs(measurement):
    '''Returns the number of significant figures in the value given'''
    if type(measurement)!=str:
        raise TypeError('Imputed measurement must be a numerical value passed \
as a string (Scientific notation allowed)')
    if '!' in measurement or '@' in measurement or '#' in measurement or '$' in\
    measurement or '%' in measurement or '&' in measurement or '(' in\
    measurement or ')' in measurement or '_' in measurement or '+' in\
    measurement or '-' in measurement or ' ' in measurement or 'm' in\
    measurement or '=' in measurement or 'Q' in measurement or 'W' in\
    measurement or 'E' in measurement or 'R' in measurement or 'T' in\
    measurement or 'Y' in measurement or 'U' in measurement or 'I' in\
    measurement or 'O' in measurement or 'P' in measurement or '[' in\
    measurement or ']' in measurement or '\'' in measurement or '{' in\
    measurement or '}' in measurement or '|' in measurement or 'A' in\
    measurement or 'S' in measurement or 'D' in measurement or 'F' in\
    measurement or 'G' in measurement or 'H' in measurement or 'J' in\
    measurement or 'K' in measurement or 'L' in measurement or ';' in\
    measurement or '\ '[0] in measurement or ':' in measurement or '"' in\
    measurement or 'Z' in measurement or 'X' in measurement or 'C' in\
    measurement or 'V' in measurement or 'B' in measurement or 'N' in\
    measurement or 'M' in measurement or ',' in measurement or '/' in\
    measurement or '<' in measurement or '>' in measurement or '?' in\
    measurement or 'q' in measurement or 'w' in measurement or 'e' in\
    measurement or 'r' in measurement or 't' in measurement or 'y' in\
    measurement or 'u' in measurement or 'i' in measurement or 'o' in\
    measurement or 'p' in measurement or 'a' in measurement or 's' in\
    measurement or 'd' in measurement or 'f' in measurement or 'g' in\
    measurement or 'h' in measurement or 'j' in measurement or 'k' in\
    measurement or 'l' in measurement or 'z' in measurement or 'x' in\
    measurement or 'c' in measurement or 'v' in measurement or 'b' in\
    measurement or 'n' in measurement:
        raise ValueError('Imputed measurement must be a numerical value passed \
as a string (Scientific notation allowed)')
    if measurement[len(measurement-2)]=='^' and measurement[len(measurement-3)]\
    =='0' and measurement[len(measurement-4)]=='1' and measurement[len(measurement-4)]=='1' #Resume: working on sci notation support
    meas_list=list(measurement)
    if meas_list==['0']:
        return 1
    else:
        while meas_list[0]=='0':
            meas_list.remove(meas_list[0])
        else:
            if '.' not in meas_list:
                reverse=meas_list[::-1]
                while reverse[0]=='0':
                    reverse.remove(reverse[0])
                else:
                    return len(reverse)
            else:
                return len(meas_list)-1
                
def to_number_sig_figs(measurement,sigfigs):
    '''Returns the measurement but to the number of significant figures given'''
    if sig_figs(measurement)<sigfigs:
        raise ValueError('Measurement must be a numerical value given as a stri\
ng and have an amount of significant greater than or equal to the amount of sig\
nificant figures given')
    meas_list=list(measurement)
    while meas_list[0]=='0':
        meas_list.remove(meas_list[0])
    else:
        if sig_figs(measurement)==sigfigs:
            remake_str=''
            for dig in meas_list:
                remake_str+=dig
            else:
                return remake_str