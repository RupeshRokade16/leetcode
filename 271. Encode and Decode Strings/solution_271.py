class Solution:
    """
    Since there can be any character coming into the encoded string, we can proceed with
    Encoding logic -
        We have the ability to add the length of the string before the start of a string
        We also need to add a delimiter to the end of the number as numbers can be of any size
    Decoding logic -
        We know for sure that the encoded string starts with a number. 
        How long of a number? - Determined by a delimiter. 
        So using pointers, we move to find the first appearance of the delimiter. That makes the
        size of the following string
        Then we can use slicing to spit out decoded strings
    """
    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            encoded_word = str(len(word)) + "$" + word
            res += encoded_word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="$":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length

        return res