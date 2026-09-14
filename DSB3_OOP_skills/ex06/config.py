num_of_steps=5

report_name='report'

report_extension='txt'

token = ""
chat_id = ""

success_message = "The report has been successfully created"
error_message = "The report hasn’t been created due to an error"

def creat_text(data,head,tail,f_head,f_tail,p_head,p_tail):
    return f"We have made {len(data)}  observations from tossing a coin: \n"\
        f"{tail} of them were tails and {head} of them were heads.\n" \
        f"The probabilities are {f_tail:.2f}% and {f_head:.2f}%, respectively.\n" \
        f"Our forecast is that in the next {num_of_steps} observations we will have: {p_tail} tail and {p_head} heads."
