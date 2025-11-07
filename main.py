from stats import get_num_words
from stats import count_characters
import sys 
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents
def sort_on(d):
    """
    A helper function for sorting that returns the 'count' value
    from a dictionary.
    """
    return d["count"]

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1] 
    kjk =get_book_text(filepath)
    # print(kjk)
    tmp=get_num_words(kjk)
    tmp2=count_characters(kjk)
    char_list=[]
    for char,count in tmp2.items():
        if char.isalpha():
            char_list.append({"char":char,"count":count})
    char_list.sort(reverse=True, key=sort_on)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count -----------")
    print(f"Found {tmp} total words")
    print("--------- Character Count --------") 
    for item in char_list:
        print(f"{item['char']}: {item['count']}")
    
    print("======== END OF REPORT =========")  
main()
print(sys.argv)
