from django.http import HttpResponse
from django.shortcuts import render

# importing user-defined modules
from . import trie
from . import pdf_reader


def homepage(request):
    # data= {}
    # try:
    #     if request.method =="POST":
    #         loc = request.POST['location']
    #         inp = request.POST['input']
    #         data['output'] = "hello"
    #     render(request,'index.html',data)
    # except Exception as e:
    #     pass
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
        inp = inp.split(" ")
        inp = pdf_reader.convert_list(inp)
        result = ""
        red_color = '\033[91m'
        end_color = '\033[0m'

        for i in inp:
            ans = t.isPresent(i)
            if(ans == False): 
                result+=i
                result += " " 
            else:
                result+=(f"{red_color}{i}{end_color} ")


        # ans = t.isPresent(inp)  

        data = {"output":result, "loc" : loc}
        print(data["output"])
        return render(request,'index.html',data)
    
    return render(request, 'index.html')

def aboutUS(request):
    return render(request, 'about.html')