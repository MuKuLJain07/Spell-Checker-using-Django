from django.http import HttpResponse
from django.shortcuts import render

# importing user-defined modules
from . import trie
from . import pdf_reader


def homepage(request):
    if request.method == "POST":
        # retrieving location and input sentence of the user from the web
        loc = request.POST.get("location")
        inp = request.POST.get("input")

        # extracting data from the pdf file and inserting it into the trie
        PDF_FILE = loc
        data = pdf_reader.pdf_data(PDF_FILE)
        data = pdf_reader.convert_list(data)

        t = trie.Trie()
        for i in range(len(data)):
            t.insert(data[i])

        # extracting words from the user input sentence and checking for each word in the trie created
        inputSentence = inp
        inp = inp.split(" ")
        inp = pdf_reader.convert_list(inp)
        result = []
        red_color = '\033[91m'
        end_color = '\033[0m'

        for i in inp:
            ans = t.isPresent(i)
            result.append({"word" : i, "bool" : str(ans)})

        # result = [{"word" : "aids", "bool" : True},{"word" : "bat", "bool" : False}]
        data = {"output":result, "loc" : loc, "inp" : inputSentence}
        print(data["output"])
        return render(request,'index.html',data)
    
    return render(request, 'index.html')

def aboutUS(request):
    return render(request, 'about.html')