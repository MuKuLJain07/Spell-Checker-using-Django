# Definition of Trie class

class TrieNode:
    def __init__(self):
        self.isTerminated = False
        self.children = []
        for i in range(26):
            self.children.append(None)


# Trie Functions
class Trie:
    def __insertHelper(self,root,str):
        temp  = root    
        for char in str:
            if(temp.children[ord(char) - ord('a')] == None):            # char is not present
                temp.children[ord(char) - ord('a')] = TrieNode()
            temp = temp.children[ord(char) - ord('a')]
        temp.isTerminated = True

    def __isPresentHelper(self, root, str):
        temp = root
        for char in str:
            if(temp.children[ord(char) - ord('a')] != None):
                temp = temp.children[ord(char) - ord('a')]
            else:
                return False
            
        return temp.isTerminated
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, str):
        self.__insertHelper(self.root, str)
    
    def isPresent(self, str):
        return self.__isPresentHelper(self.root, str)




import pdf_reader
PDF_FILE = "E:\Projects\Spell Checker\Spell_Checker\static\dataset\words.pdf"
data = pdf_reader.pdf_data(PDF_FILE)

# convert each word of the pdf file into lowercase and remove extra spaces from each word
for i in range(len(data)):
    data[i] = data[i].lower()
    data[i] = data[i].replace(" ","")

t = Trie()
for i in range(len(data)):
    t.insert(data[i])

ans = t.isPresent("aids")
print(ans)  


