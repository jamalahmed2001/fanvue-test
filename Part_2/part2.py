import pandas as pd

# load CSV file
df = pd.read_csv('fan_creator_chat.csv')
df = df.sort_values('timestamp')

processed_messages = []
prev_sender = None
prev_msg = ''
#merge adjacent messages from the same sender
for index, row in df.iterrows():
    if row['sender_handle'] == prev_sender:
        # Concatenate the message with a space
        prev_msg += " " + row['message']
    else:
        # If the sender has changed save the current message
        if prev_sender is not None:
            processed_messages.append({'sender_handle': prev_sender, 'message': prev_msg})
        # Update the current sender and message
        prev_sender = row['sender_handle']
        prev_msg = row['message']
processed_messages.append({'sender_handle': prev_sender, 'message': prev_msg})
merged_df = pd.DataFrame(processed_messages)
#split fan and creator msgs
fan_df = merged_df.loc[merged_df['sender_handle'] == 'fan']
creator_df = merged_df.loc[merged_df['sender_handle'] == 'creator']
output = []
#store in json format
for i in range(0,len(fan_df)):
    fan_msg = fan_df.iloc[i]['message']
    creator_msg = creator_df.iloc[i]['message']
    row = ' {"messages": [{"role": "system", "content": "Jada is a creator on Fanvue, chatting with one of her fans."}, {"role": "user", "content":"'+ fan_msg+'"}, {"role": "assistant", "content":"'+ creator_msg+ '"}]}'
    output.append(row)
#write to file
f = open('fan_creator_chat.json','w')
for row in output:
    f.write(row+'\n')
f.close()