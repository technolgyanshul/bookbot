def get_num_words(file_words):
    fwords_total=file_words.split()
    m=0
    for i in fwords_total:
        m+=1
    
    return m
    
def count_characters(text):
    char_counts={}
    lower_text=text.lower()
    for char in lower_text:
        if char in char_counts:
            char_counts[char]+=1
        else :
            char_counts[char]=1
    
    return char_counts
