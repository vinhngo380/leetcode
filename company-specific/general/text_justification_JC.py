class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        Close, Initial Try!
        arrayOfWords = []
        temp, tempChars = [], 0
        i = 0
        while i < len(words):
            proposedLine = len(words[i]) + len(temp) + tempChars
            if proposedLine < maxWidth: # length of the current word + total number of words (# reserved for space) + total number of current characters
                temp.append(words[i])
                tempChars += len(words[i])
            else: # too many words/exceeds width
                # first identify how many space justification
                toBeAdded = ""
                if len(temp) > 1:
                    spaceBetween = "".join([" "] * ((abs(maxWidth-tempChars)) // (len(temp)-1)))
                    if len(spaceBetween) % (len(temp) - 1) == 1: # extra space required
                        temp[0] += " "
                    toBeAdded = spaceBetween.join(temp)
                else:
                    spaceRemaining = "".join([" "] * (maxWidth - len(temp[0])))
                    toBeAdded = temp[0] + spaceRemaining
                arrayOfWords.append(toBeAdded)
                temp, tempChars = [], 0
                i -= 1
            i += 1

        lastLine = temp[0] + "".join([" "] * (maxWidth - len(temp[0])))
        arrayOfWords.append(lastLine)
    
        return arrayOfWords
        '''
        
        res = []
        line, line_chars = [], 0
        for i in range(len(words)):
            # if exceeds maxWidth -> all chars in line, len(line) (which is space), curr word
            if line_chars + len(line) + len(words[i]) > maxWidth:
                spaces = (maxWidth - line_chars) // max(1, len(line) - 1)
                remainder = (maxWidth - line_chars) % max(1,len(line)-1)
                # adding the spaces, justifying
                for j in range(max(1, len(line) - 1)): # Need to run at least once in case len(line) == 1, thus usage of max
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                res.append("".join(line))
                line, line_chars = [], 0
            line.append(words[i])
            line_chars += len(words[i])
        # left justified, last line
        last_line = " ".join(line)
        trailing = maxWidth - len(last_line)
        res.append(last_line + (" " * trailing))
        return res

'''
TLDR: Did with help from NeetCode. Focus and remember the specific edge cases (last line, single word, extra space distribution). Also understand--not just remember--
how the space computation (space, remainder) is processed. Utilize max() in cases where we have modulo or divisor 0.

TC O(n)
SC O(n)
'''
            
