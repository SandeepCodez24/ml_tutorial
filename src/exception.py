import sys
# sys module provides various functions and variables that are used to mainpulate different parts of python runtime environment

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #this function provides the info of error 1.from which file and line the error has been ocurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
